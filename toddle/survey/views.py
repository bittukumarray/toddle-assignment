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
        try:
            survey_name = request.data['survey_name']
            questions_data = request.data['questions']
        except:
            return Response({"msg":"data format was not correct"}, status=status.HTTP_400_BAD_REQUEST)
        final_out={}
        survey = Survey.objects.create(created_by=request.user, name=survey_name)
        survey.save()
        final_out["survey_id"]=survey.id
        questions=[]
        try:
            for eachQ in questions_data:
                obj = Question.objects.create(title=eachQ['title'], survey=survey)
                obj.save()
                Q_dict={"Q_id":obj.id, "Q_title":obj.title}
                questions.append(Q_dict)
            final_out["questions"]=questions
            return Response(final_out, status=status.HTTP_201_CREATED)
        except:
            return Response({"msg":"Some questions data format were not correcr"}, status=status.HTTP_400_BAD_REQUEST)


class SurveyResult(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        survey=""
        try:
            survey = Survey.objects.get(id=id)
        except:
            return Response({"msg":"Survey id was not correct"}, status=status.HTTP_400_BAD_REQUEST)
        final_result = {"survey_id":id}
        questions_list = Question.objects.filter(survey=survey)
        questions=[]
        for Qs in questions_list:
            eachQ_data = {"Q_id":Qs.id, "Q_title":Qs.title, "true_resp":0, "false_resp":0}
            QRObj = QuestionResponse.objects.filter(question=Qs)
            for eachQR in QRObj:
                if eachQR.ans_given==True:
                    eachQ_data['true_resp']+=1
                else:
                    eachQ_data['false_resp']+=1
            questions.append(eachQ_data)
        final_result["questions"]=questions

        return Response(final_result)




class TakeSurvey(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        survey=""
        try:
            survey = Survey.objects.get(id=request.data['survey_id'])
        except:
            return Response({"msg":"survey id is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        survey_response = SurveyResponse.objects.create(survey=survey, respondent=user)
        survey_response.save()
        questions_data =[]
        try:
            questions_data = request.data['questions']
            for eachQ in questions_data:
                question = Question.objects.get(id=eachQ['question_id'], survey=survey)
                question_response = QuestionResponse.objects.create(respondent=user, survey_response=survey_response, question=question, ans_given=eachQ['ans_given'])
                question_response.save()
            return Response({"msg":"You took survey successfully"})
        except KeyError:
            return Response({"msg":"data format were not correct"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"msg":"Some question Id were wrong"}, status=status.HTTP_400_BAD_REQUEST)