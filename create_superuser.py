import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fittrack_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create admin superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@gmail.com',
        password='admin1005'
    )
    print("✅ Admin superuser created successfully!")
    print("Username: admin")
    print("Email: admin@gmail.com")
else:
    print("ℹ️ Admin user already exists - skipping creation")