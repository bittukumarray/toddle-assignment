from django.contrib import admin
from .models import *

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(SurveyResponse)
admin.site.register(QuestionResponse)

# Register your models here.
