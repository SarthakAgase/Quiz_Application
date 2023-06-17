from django.contrib import admin
from .models import *

# Register your models here.

class AnswerInLine(admin.TabularInline):
    model=Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]


admin.site.register(questions, QuestionAdmin)
admin.site.register(Answer)
