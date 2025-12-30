from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from workouts import views as workout_views
from goals import views as goal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('users.urls')),
    
    path('', workout_views.home, name='home'),
    path('dashboard/', workout_views.dashboard, name='dashboard'),
    
    path('workouts/', workout_views.workout_list, name='workout_list'),
    path('workouts/<int:pk>/', workout_views.workout_detail, name='workout_detail'),
    path('workouts/new/', workout_views.workout_create, name='workout_create'),
    path('workouts/<int:pk>/edit/', workout_views.workout_update, name='workout_update'),
    path('workouts/<int:pk>/delete/', workout_views.workout_delete, name='workout_delete'),
    
    path('goals/', goal_views.goal_list, name='goal_list'),
    path('goals/new/', goal_views.goal_create, name='goal_create'),
    path('goals/<int:pk>/edit/', goal_views.goal_update, name='goal_update'),
    path('goals/<int:pk>/delete/', goal_views.goal_delete, name='goal_delete'),
    path('goals/<int:pk>/complete/', goal_views.goal_complete, name='goal_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'fittrack_project.views.custom_404'
handler500 = 'fittrack_project.views.custom_500'
