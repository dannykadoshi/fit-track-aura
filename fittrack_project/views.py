from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json


@require_http_methods(["GET"])
def manifest(request):
    """Serve the Web App Manifest for PWA"""
    manifest_data = {
        "name": "FitTrack Aura",
        "short_name": "FitTrack",
        "description": "Track your fitness journey with FitTrack Aura. Set goals, log workouts, and earn badges.",
        "start_url": "/",
        "scope": "/",
        "display": "standalone",
        "orientation": "portrait-primary",
        "theme_color": "#a855f7",
        "background_color": "#1a1a1a",
        "icons": [
            {
                "src": "/static/images/favicon-16x16.png",
                "sizes": "16x16",
                "type": "image/png"
            },
            {
                "src": "/static/images/favicon-32x32.png",
                "sizes": "32x32",
                "type": "image/png"
            },
            {
                "src": "/static/images/apple-touch-icon.png",
                "sizes": "180x180",
                "type": "image/png"
            },
            {
                "src": "/static/images/fittrack-icon-512.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any"
            }
        ],
        "screenshots": [
            {
                "src": "/static/images/og-image.png",
                "type": "image/png",
                "sizes": "1200x630"
            }
        ],
        "categories": ["fitness", "health"],
        "shortcuts": [
            {
                "name": "Log Workout",
                "short_name": "Log Workout",
                "description": "Quickly log a new workout",
                "url": "/workouts/new/",
                "icons": []
            },
            {
                "name": "View Goals",
                "short_name": "Goals",
                "description": "View your fitness goals",
                "url": "/goals/",
                "icons": []
            }
        ]
    }
    return JsonResponse(manifest_data)


def custom_404(request, exception):
    """Custom 404 error handler"""
    return render(request, 'errors/404.html', status=404)


def custom_500(request):
    """Custom 500 error handler"""
    return render(request, 'errors/500.html', status=500)
