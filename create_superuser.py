from django.contrib.auth import get_user_model
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fittrack_project.settings')
django.setup()


User = get_user_model()

# Admin user should already exist from first deployment
# This script only runs once
if not User.objects.filter(username='admin').exists():
    print("⚠️ Admin user not found - create manually via Django admin")
else:
    print("ℹ️ Admin user exists - ready to use")
