from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import DiarySerializer, AiSerializer
from .models import Diary, Ai

# Create your views here.

class DiaryList(APIView): # 목록 보여줌
    def get(self, request): # 리스트 보여줄 때
        diaries = Diary.objects.all()

        serializers = DiarySerializer(diaries, many=True) # 여러개 객체 serialize하려면 many=Ture
        return Response(serializers.data)

    def post(self, request): # 새 글 작성시
        serializer = DiarySerializer(
            data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

class DiaryDetail(APIView):
    def get_object(self, pk): # 일기 객체 가져오기
        try:
            return Diary.obejcts.get(pk=pk)
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
    
class AiDetail(APIView):
    def get_object(self, pk): # Ai 응답 객체 가져오기
        try:
            return Ai.obejcts.get(pk=pk)
        except Ai.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None): # detail 보기
        ai = self.get_object(pk)
        serializer = AiSerializer(ai)
        return Response(serializer.data)