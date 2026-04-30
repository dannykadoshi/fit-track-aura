// Service Worker for FitTrack Aura PWA
const CACHE_NAME = 'fittrack-aura-v1';
const urlsToCache = [
  '/',
  '/static/css/bootstrap.min.css',
  '/static/css/style.css',
  '/offline.html'
];

// Install event - cache essential files
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(urlsToCache).catch(() => {
        // If offline.html doesn't exist, continue anyway
        return cache.addAll(urlsToCache.filter(url => url !== '/offline.html'));
      });
    })
  );
  self.skipWaiting();
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  // Skip non-GET requests
  if (event.request.method !== 'GET') {
    return;
  }

  event.respondWith(
    caches.match(event.request).then((response) => {
      if (response) {
        return response;
      }

      return fetch(event.request)
        .then((response) => {
          // Don't cache if not a success response
          if (!response || response.status !== 200 || response.type === 'error') {
            return response;
          }

          // Clone the response
          const responseToCache = response.clone();

          // Cache GET requests for static assets and HTML pages
          if (event.request.method === 'GET' && 
              (event.request.url.includes('/static/') || 
               event.request.url.endsWith('/') ||
               event.request.url.includes('/dashboard') ||
               event.request.url.includes('/goals') ||
               event.request.url.includes('/workouts'))) {
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, responseToCache);
            });
          }

          return response;
        })
        .catch(() => {
          // Return offline page if available, otherwise a generic response
          return caches.match('/offline.html').catch(() => {
            return new Response(
              'You are offline. Please check your internet connection.',
              { status: 503, statusText: 'Service Unavailable' }
            );
          });
        });
    })
  );
});
