# Generated by Django 3.0.3 on 2020-02-19 10:27

import answersheet.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answersheet', '0002_answersheet_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to=answersheet.models.AnswerKey.getImagePath)),
            ],
        ),
        migrations.RemoveField(
            model_name='answersheet',
            name='image1',
        ),
    ]
