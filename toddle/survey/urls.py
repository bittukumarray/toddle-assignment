from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.CreateSurvey.as_view()),
    path('get-result/<int:id>',views.SurveyResult.as_view()),
    path('take/',views.TakeSurvey.as_view()),
]
