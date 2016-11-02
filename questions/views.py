from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Question,Answer
from .forms import QuestionForm, AnswerForm


# Create your views here.

def manage(request,):
    quest = Question()
    ans = Answer()
    
    questions = []
    for question in Question.objects.all():
    	questions.append((question,question.answers.filter()))

    qform = QuestionForm(instance=quest)
    ansform = AnswerForm(instance=ans) 
    if request.method == 'POST':
    	if 'answer' in request.POST.keys():
            form = AnswerForm(request.POST, instance=ans)
            if form.is_valid():
                answer = request.POST.get('answer')
                return redirect('manage')
            else:
            	return render(request, 'questions/manage.html',
                    {'questions': questions,
                    'qform':qform,
                    'ansform': ansform,
                    'invalid':form,
                    'pk': int(request.POST.get('pk')),
                    })
        elif 'question' in request.POST.keys():
            form = QuestionForm(request.POST, instance=quest)

            if form.is_valid():
                question = request.POST.get('question')

                return redirect('manage')
            else:
            	return render(request, 'questions/manage.html',
                    {'questions': questions,
                    'qform': form,
                    'ansform': ansform,
                    })
    
    else:
        return render(request, 'questions/manage.html',
            {'questions': questions,
            'qform':qform,
            'ansform': ansform,
            })


def questions(request, question_number=None):
	pass


@require_http_methods(["POST"])
def add_question(request):
	pass

@require_http_methods(["GET"])
def make_right(request, answer_pk, question_pk):
	pass
