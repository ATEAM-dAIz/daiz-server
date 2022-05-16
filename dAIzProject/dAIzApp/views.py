from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django.http import Http404
import json

from .serializers import DiarySerializer, AiSerializer
from .models import Diary, Ai

from dAIzApp.ai.daiz import Situation, Emotion, Comment

# Create your views here.

@permission_classes((IsAuthenticated, ))
@authentication_classes((JWTTokenUserAuthentication,))
class DiaryList(APIView): # 목록 보여줌
    def get(self, request): # 리스트 보여줄 때
        print(request.user.pk)
        diaries = Diary.objects.filter(user = request.user.pk)

        serializers = DiarySerializer(diaries, many=True) # 여러개 객체 serialize하려면 many=Ture
        return Response(serializers.data)
    
    def post(self, request): # 새 글 작성시
        data = json.loads(request.body)
        content = data['content'] # requset에서 content만 가져와서
        DiaryData = {
            'user' : request.user.pk,
            'title' : data['title'],
            'content' : content
        }
        
        # 모델에 넣음
        situation = Situation(content)
        emotion = Emotion(content)
        comment = Comment(content)
        
        serializer_Diary = DiarySerializer(data = DiaryData)

        if serializer_Diary.is_valid():
            serializer_Diary.save()
            AiData = { # 모델 결과를 딕셔너리로 통합
                'did' : serializer_Diary.data['id'],
                'situation' : situation,
                'emotion' : emotion,
                'comment' : comment
            }
            serializer_Ai = AiSerializer(data = AiData)
            if serializer_Ai.is_valid():
                serializer_Ai.save() # Ai 테이블에 저장
            return Response(serializer_Diary.data, status=status.HTTP_201_CREATED)
        return Response(serializer_Diary.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated, ))
@authentication_classes((JWTTokenUserAuthentication,))
class DiaryDetail(APIView):
    def get_object(self, pk): # 일기 객체 가져오기
        try:
            return Diary.objects.get(pk=pk)
        except Diary.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None): # 일기 detail 보기
        diary = self.get_object(pk)
        serializer = DiarySerializer(diary)
        return Response(serializer.data)

    def delete(self, request, pk, format=None): # 일기 삭제하기
        diary = self.get_object(pk)
        diary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-------------------------------------------------------------------------------------------------

@permission_classes((IsAuthenticated, ))
@authentication_classes((JWTTokenUserAuthentication,))
class AiDetail(APIView):
    def get_object(self, pk): # Ai 응답 객체 가져오기
        try:
            return Ai.objects.filter(did=pk)
        except Ai.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None): # detail 보기
        ai = self.get_object(pk)
        serializer = AiSerializer(ai, many=True)
        return Response(serializer.data)