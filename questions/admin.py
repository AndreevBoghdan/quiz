from django.contrib import admin
from models import Answer, Question, Statistic, Quiz


class QuestionAdmin(admin.ModelAdmin):
    """
    Question admin
    """
    fields=['question', 'quiz']
    list_display = ( 'question', 'count', 'statistics')

admin.site.register(Question, QuestionAdmin)

class QuizAdmin(admin.ModelAdmin):
    """
    Quiz admin
    """

admin.site.register(Quiz, QuizAdmin)

class AnswerAdmin(admin.ModelAdmin):
    """
    Answer admin
    """
    fields=['question', 'answer']
    
    list_display = ('answer',)

admin.site.register(Answer, AnswerAdmin)

class StatisticAdmin(admin.ModelAdmin):
    """
    Statistic admin
    """


admin.site.register(Statistic, StatisticAdmin)