from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

# Create your views here.

class CreateSurvey(APIView):
    def post(self, request):
        return Response({"data":"data"})

class SurveyResult(APIView):
    def get(self, request):
        return Response({"data":"data"})


class TakeSurvey(APIView):
    def get(self, request):
        return Response({"data":"data"})