from django import forms

from django.forms import ModelForm, Form
from django.forms.widgets import TextInput

from .models import Question, Answer


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = (
                  'question',
                  )


    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        self.fields['question'].widget = TextInput(attrs={
            'placeholder': 'Question'})

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = (
                  'answer',
                  )


    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        self.fields['answer'].widget = TextInput(attrs={
            'placeholder': 'Answer'})
