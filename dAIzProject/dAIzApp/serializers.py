from rest_framework import serializers
from .models import Review, User, Diary, Ai
from rest_framework_simplejwt.tokens import RefreshToken
from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'updated_at')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CustomTokenRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh_token'])
        data = {'access_token': str(refresh.access_token)}

        return data

class LoginSerializer(RestAuthLoginSerializer):
    username = None

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = "__all__"

class AiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ai
        fields = "__all__"
