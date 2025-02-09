from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('organizer', 'Organizer'),
        ('attendee', 'Attendee'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='attendee', blank=False, null=False)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"