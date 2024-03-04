from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from datetime import datetime, timedelta
from django.contrib.auth.models import UserManager

class Users(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']
    
    class Meta:
        db_table = 'users'

class UserActivateTokensManager(models.Manager):
    
    def activate_user_by_token(self, token):
        user_activate_token = self.filter(
            token=token,
            expired_at__gte=datetime.now()
        ).first()
        if user_activate_token:
            user = user_activate_token.user
            user.is_active = True
            user.save()
            return user
        return None

class UserActivateTokens(models.Model):
    
    token = models.UUIDField(db_index=True, default=uuid4)
    expired_at = models.DateTimeField()
    user = models.ForeignKey(
        'Users', on_delete=models.CASCADE
    )
    
    objects = UserActivateTokensManager()
    
    class Meta:
        db_table = 'user_activate_token'
        
@receiver(post_save, sender=Users)
def publish_token(sender, instance, **kwargs):
    user_activate_token = UserActivateTokens.objects.create(
        user=instance, expired_at=datetime.now() + timedelta(days=1)
    )
    # メールでURLを送信するなど、適切なアクティベーション手段を選択してください
    print(f'Activate user URL: https://127.0.0.1:8000/accounts/activate_user/{user_activate_token.token}')
