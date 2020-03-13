from django import forms
from answersheet.models import *

class AnswerKeyUploadForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Question Name'
            }),
        help_text='For furture reference'
    )
    image = forms.ImageField(
         widget=forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Question Name'
        })
    )


class AnswerSheetUploadForm(forms.Form):
    answerKey = forms.ModelChoiceField(queryset=AnswerKey.objects.all())
    image = forms.ImageField()


class UserNameAndPassword(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
class UserNameAndPasswordFromTestLogin(forms.Form):
    test_login_user_name=forms.CharField()
    test_login_password=forms.CharField()