from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DiaryList, DiaryDetail, AiDetail

urlpatterns = [
    path('signup/', include('dj_rest_auth.registration.urls')), # 회원가입
    
    path('diary/', DiaryList.as_view()),
    path('diary/<int:pk>/', DiaryDetail.as_view()),
    path('ai/<int:pk>/', AiDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
