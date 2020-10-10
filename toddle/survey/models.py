from django.db import models

# Create your models here.


class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    opt1 = models.BooleanField(default=False)
    opt2 = models.BooleanField(default=True)
    ans_given = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.title



