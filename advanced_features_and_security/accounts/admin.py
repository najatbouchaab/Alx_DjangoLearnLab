from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Admin interface for CustomUser model.
    """
    model = CustomUser
    
    # Display these fields in the user list view
    list_display = [
        'username', 
        'email', 
        'first_name', 
        'last_name', 
        'date_of_birth', 
        'is_staff', 
        'is_active'
    ]
    
    # Add filters in the right sidebar
    list_filter = [
        'is_staff', 
        'is_superuser', 
        'is_active', 
        'date_joined'
    ]
    
    # Enable search functionality
    search_fields = [
        'username', 
        'email', 
        'first_name', 
        'last_name'
    ]
    
    # Default ordering
    ordering = ['username']
    
    # Fieldsets for editing existing users
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal Information', {
            'fields': (
                'first_name', 
                'last_name', 
                'email', 
                'date_of_birth', 
                'profile_photo'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active', 
                'is_staff', 
                'is_superuser', 
                'groups', 
                'user_permissions'
            )
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    # Fieldsets for creating new users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 
                'email', 
                'password1', 
                'password2', 
                'date_of_birth', 
                'profile_photo', 
                'is_staff', 
                'is_active'
            )
        }),
    )


# Register CustomUser with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)