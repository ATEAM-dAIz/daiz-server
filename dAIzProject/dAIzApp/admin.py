from django.contrib import admin
from .models import Review, User, Diary, Ai

# Register your models here.
admin.site.register(Review)
admin.site.register(User)
admin.site.register(Diary)
admin.site.register(Ai)