from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Quiz(models.Model):
    class Meta():
        db_table = 'quiz'

    name = models.CharField(max_length=200, default='new Quiz')
    headline = models.CharField(max_length=100, default='Quiz Headline')

    def __str__(self):
        return self.name

class Statistic(models.Model):
    class Meta():
        db_table = 'stat'

    right = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    percent = models.IntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=True):
        try:    
            self.percent = self.right * 100 / self.total
        except ZeroDivisionError:
            self.percent = 0
        super(Statistic, self).save()

    def __str__(self):
        return str(self.percent)

class Question(models.Model):
    class Meta():
        db_table = 'question'
    question = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    statistics = models.ForeignKey(Statistic, related_name='stat')
    quiz = models.ForeignKey(Quiz, related_name='quiz')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=True):
        if self.answers is None:
            self.count = 0
        else:
            self.count = len(Answer.objects.filter(question=self))
        super(Question, self).save()

    def __str__(self):
        return self.question

class Answer(models.Model):
    class Meta():
        db_table = 'answer'
    answer = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='answers')
    is_Correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
