import os
import django
from django.apps import apps

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DriveDuWish.settings')  # Replace 'DriveDuWish' with your project name
django.setup()

# Define the model name and username you want to filter
model_name = "User"
username_to_find = "thorgrim"

# Iterate through all registered models
for model in apps.get_models():
    if model.__name__ == model_name:  # Check for the specific model name
        print(f"Model: {model.__name__}")
        
        # Query the database for the specific username
        try:
            user = model.objects.get(username=username_to_find)
            print(f"Username: {user.username}")
            print(f"Email: {user.email}")
            print(f"Other details: {user}")  # Customize this as needed to print more fields
        except model.DoesNotExist:
            print(f"No user with username '{username_to_find}' found.")