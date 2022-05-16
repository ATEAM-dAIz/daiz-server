from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DiaryList, DiaryDetail, AiDetail

urlpatterns = [
    path('signup/', include('dj_rest_auth.registration.urls')), # 회원가입
    path('signup', include('dj_rest_auth.registration.urls')), # 회원가입
    
    path('diary/', DiaryList.as_view()), # 일기 목록
    path('diary/<int:pk>/', DiaryDetail.as_view()), # 특정 일기              pk : 일기id
    path('diary/<int:pk>/ai/', AiDetail.as_view()), # 특정 일기의 AI결과      pk : 일기id
]

urlpatterns = format_suffix_patterns(urlpatterns)
