# Generated by Django 3.0.6 on 2020-10-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='survey',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]