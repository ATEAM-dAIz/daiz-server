from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReviewList, ReviewDetail

urlpatterns = [
    path('review/', ReviewList.as_view()),
    path('review/<int:pk>/', ReviewDetail.as_view()),
    
    path('signup/', include('dj_rest_auth.registration.urls')), # 회원가입
]

urlpatterns = format_suffix_patterns(urlpatterns)
