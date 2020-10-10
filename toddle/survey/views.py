from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework import status


# Create your views here.

class CreateSurvey(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        survey_name=""
        questions_data=[]
        print(request.data)
        try:
            survey_name = request.data['survey_name']
            questions_data = request.data['questions']
        except:
            return Response({"msg":"data format was not correct"}, status=status.HTTP_400_BAD_REQUEST)
        survey = Survey.objects.create(name=survey_name)
        survey.save()

        try:
            for eachQ in questions_data:
                obj = Question.objects.create(title=eachQ['title'], survey=survey)
                obj.save()
            return Response({"msg":"The survey created successfully"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"msg":"Some questions data format were not correcr"}, status=status.HTTP_400_BAD_REQUEST)




class SurveyResult(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({"data":"data"})


class TakeSurvey(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response({"data":"data"})