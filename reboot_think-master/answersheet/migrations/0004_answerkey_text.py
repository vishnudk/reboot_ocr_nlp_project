# Generated by Django 3.0.3 on 2020-02-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answersheet', '0003_auto_20200219_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerkey',
            name='text',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
