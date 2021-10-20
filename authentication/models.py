from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.


class CustomUserManager(BaseUserManager):
    """Custom User Manager for Custome User model"""

    def create_user(self, user_id, password, name=None, email=None, **kwargs):
        if not user_id:
            raise ValueError('User must have valid user ID')

        user = self.model(user_id=user_id, name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, name=None, email=None,  **kwargs):
        user = self.create_user(
            user_id=user_id, password=password, name=name, email=email)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, user_id, password, name=None, email=None,  **kwargs):
        user = self.create_user(
            user_id=user_id, password=password, name=name, email=email)
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(PermissionsMixin, AbstractBaseUser):
    """Custom User model that identifies user by User ID"""
    user_id = models.CharField(
        verbose_name='User ID', unique=True, max_length=32)
    name = models.CharField(verbose_name='User name',
                            max_length=255, null=True, blank=True)
    email = models.EmailField(
        max_length=255, verbose_name='Email address', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.user_id

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label: str) -> bool:
        return self.is_staff


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)
