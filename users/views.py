from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserUpdateForm, ProfileUpdateForm


@login_required
def profile_view(request):
    """Display and edit user profile"""
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated! ✅')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    # Calculate active goals count
    active_goals_count = request.user.goals.filter(is_completed=False).count()
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'active_goals_count': active_goals_count,
    }
    
    return render(request, 'users/profile.html', context)


@login_required
def change_password(request):
    """Change user password"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated! 🔒')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form,
    }
    
    return render(request, 'users/change_password.html', context)


@login_required
def toggle_theme(request):
    """Toggle between dark and light theme"""
    profile = request.user.profile
    
    if profile.theme == 'dark':
        profile.theme = 'light'
        messages.success(request, '☀️ Switched to Light Mode')
    else:
        profile.theme = 'dark'
        messages.success(request, '🌙 Switched to Dark Mode')
    
    profile.save()
    
    # Redirect back to the page they came from
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))
