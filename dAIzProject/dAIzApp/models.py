from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    
class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(verbose_name='email', unique=True)
    name = models.CharField(default="", max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email' # email로 로그인
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.id)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
class Diary(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.ForeignKey('User', related_name='user', on_delete=models.CASCADE, db_column='uid')
    title = models.CharField(max_length=50, default='제목 없음')
    content = models.TextField(max_length=200, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    
class Ai(models.Model):
    id = models.BigAutoField(primary_key=True)
    did = models.ForeignKey('Diary', related_name='diary', on_delete=models.CASCADE, db_column='did')
    situation = models.CharField(max_length=50, null=False)
    emotion = models.CharField(max_length=50, null=False)
    comment = models.CharField(max_length=1000, null=False)
    
    