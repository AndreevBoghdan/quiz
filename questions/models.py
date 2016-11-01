from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    class Meta():
        db_table = 'question'
    question = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=True):
        if self.answers is None:
            self.count = 0
        else:
            self.count = len(self.answers)
        super(Question, self).save()

class Answer(models.Model):
	class Meta():
		db_table = 'answer'
	answer = models.CharField(max_length=200)
	question = models.ForeignKey(Question, related_name='answers')
	is_Correct = models.BooleanField(default=False)
