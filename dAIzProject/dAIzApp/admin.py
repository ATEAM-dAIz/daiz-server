from django.contrib import admin
from .models import User, Diary, Ai

# Register your models here.
admin.site.register(User)
admin.site.register(Diary)
admin.site.register(Ai)