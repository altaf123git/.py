from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin, BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, mobile, password=None, **extra_fields):
        if not mobile:
            raise ValueError('The Mobile field must be set')
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(mobile, password, **extra_fields)


class Cust(AbstractUser, PermissionsMixin):
    city=models.CharField(max_length=50)
    mobile=models.CharField(unique=True, max_length=50)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['username']
