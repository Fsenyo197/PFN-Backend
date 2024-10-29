import os
import django

# Set the default settings module for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pfn.settings')

# Set up Django
django.setup()

from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model

User = get_user_model()

def generate_admin_token(username):
    try:
        admin_user = User.objects.get(username=username)
        token = AccessToken.for_user(admin_user)
        return token
    except User.DoesNotExist:
        print(f'User "{username}" does not exist.')
        return None

if __name__ == '__main__':
    admin_username = input("Enter the admin username: ") 
    token = generate_admin_token(admin_username)
    if token:
        print(f'Generated JWT token for user "{admin_username}": {token}')
