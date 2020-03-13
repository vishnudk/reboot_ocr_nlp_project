from django.contrib import admin

from .models import *


@admin.register(AnswerKey)
class AnswerKeyAdmin(admin.ModelAdmin):
    pass


@admin.register(AnswerSheet)
class AnswerSheetAdmin(admin.ModelAdmin):
    pass

