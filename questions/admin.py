from django.contrib import admin
from models import Answer, Question, Statistic


class QuestionAdmin(admin.ModelAdmin):
    """
    Question admin
    """
    fields=['question',]
    list_display = ( 'question', 'count', 'statistics')

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    """
    Answer admin
    """
    fields=['question', 'answer']
    
    list_display = ('answer',)

admin.site.register(Answer, AnswerAdmin)

class StatisticAdmin(admin.ModelAdmin):
    """
    Answer admin
    """


admin.site.register(Statistic, StatisticAdmin)