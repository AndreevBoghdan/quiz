from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Question,Answer
from .forms import QuestionForm, AnswerForm


# Create your views here.

@require_http_methods(["GET"])
def manage(request):
    quest = Question()
    ans = Answer()
    questions = []
    for question in Question.objects.all():
    	questions.append((question,question.answers.filter()))
    qform = QuestionForm(instance=quest)
    ansform = AnswerForm(instance=ans)
    return render(request, 'questions/manage.html',
                {'questions': questions,
                'qform':qform,
                'ansform': ansform,
                })

def questions(request, question_number=None):
	pass

@require_http_methods(["POST"])
def add_answer(request, question_pk):
	pass

@require_http_methods(["POST"])
def add_question(request):
	pass

@require_http_methods(["GET"])
def make_right(request, answer_pk, question_pk):
	pass
