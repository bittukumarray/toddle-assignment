from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class SurveyResponse(models.Model):
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    respondent = models.ForeignKey(User, on_delete=models.CASCADE)


class QuestionResponse(models.Model):
    id = models.AutoField(primary_key=True)
    survey_response = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    respondent = models.ForeignKey(User, on_delete=models.CASCADE)
    ans_given = models.BooleanField(blank=True, null=True)
