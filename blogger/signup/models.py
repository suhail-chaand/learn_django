from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class BlogUserManager(BaseUserManager):

    def create_user(self, email, phone, first_name, last_name, password=None):

        if not email:
            raise ValueError('Email is a required field')
        
        user = self.model(
            email=self.normalize_email(email), 
            phone=phone,
            first_name=first_name,
            last_name=last_name
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, first_name, last_name, password=None):

        user = self.create_user(
            email,
            phone,
            first_name,
            last_name,
            password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class BlogUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=10)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = BlogUserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm_lidt, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin