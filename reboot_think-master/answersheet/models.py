import uuid
from django.db import models


class AnswerKey(models.Model):
    def getImagePath(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return 'static/images/answer-keys/' + filename

    name = models.CharField(max_length=5)
    image = models.ImageField(upload_to=getImagePath, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class AnswerSheet(models.Model):
    def getImagePath(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return 'static/images/answer-sheets/' + filename
    
    key = models.ForeignKey(AnswerKey, on_delete=models.PROTECT, null=True, blank=True)
    image =models.ImageField(upload_to=getImagePath, null=True, blank=True)
    marks = models.FloatField(null=True, blank=True)
    summ=models.TextField(null=True, blank=True)
    

class test_login_data(models.Model):
    user_name_from_test_login=models.CharField(max_length=100)
    password_from_test_login=models.CharField(max_length=100)

