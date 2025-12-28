"""
URL configuration for fittrack_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from workouts import views as workout_views
from goals import views as goal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # Homepage & Dashboard
    path('', workout_views.home, name='home'),
    path('dashboard/', workout_views.dashboard, name='dashboard'),

    # Workout URLs
    path('workouts/', workout_views.workout_list, name='workout_list'),
    path('workouts/<int:pk>/', workout_views.workout_detail, name='workout_detail'),
    path('workouts/new/', workout_views.workout_create, name='workout_create'),
    path('workouts/<int:pk>/edit/', workout_views.workout_update, name='workout_update'),
    path('workouts/<int:pk>/delete/', workout_views.workout_delete, name='workout_delete'),

    # Goal URLs
    path('goals/', goal_views.goal_list, name='goal_list'),
    path('goals/new/', goal_views.goal_create, name='goal_create'),
    path('goals/<int:pk>/edit/', goal_views.goal_update, name='goal_update'),
    path('goals/<int:pk>/delete/', goal_views.goal_delete, name='goal_delete'),
    path('goals/<int:pk>/complete/', goal_views.goal_complete, name='goal_complete'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Error handlers
handler404 = 'fittrack_project.views.custom_404'
handler500 = 'fittrack_project.views.custom_500'
