from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Question,Answer
from .forms import QuestionForm, AnswerForm
import signals


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
                question = Question.objects.get(pk=request.POST.get('pk'))
                Answer.objects.create(answer=answer, question=question)
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
                Question.objects.create(question=question)

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

def end_page(request, right, total):
	return render(request, 'questions/end_page.html',
                    {'right': right,
                    'total': total
                    })

def questions(request):
    questions = []
    for question in Question.objects.filter(count__gte=1):
        questions.append((question,question.answers.filter()))

    if request.method == "POST":
        right_count= 0
        total = len(Question.objects.filter(count__gte=1))

        for question in Question.objects.filter(count__gte=1):
            user_answer = request.POST.get('answer-on-' + str(question.pk))
            right_answer = Answer.objects.get(question=question, is_Correct=True)
            if right_answer.answer == user_answer:
                right_count += 1
                question.statistics.right += 1
            question.statistics.total += 1
            question.statistics.save()

    	return redirect('end_page', right=right_count, total=total)
        
    else:
        return render(request, 'questions/quiz.html',
                        {'questions': questions,
                        })



@require_http_methods(["GET"])
def make_right(request, answer_pk, question_pk):
    question = Question.objects.get(pk=question_pk)
    answers = Answer.objects.filter(question=question)
    for answer in answers:
        answer.is_Correct = False
        answer.save()
	answer = Answer.objects.get(pk=answer_pk)
	answer.is_Correct = True
	answer.save()
    return redirect('manage')


@require_http_methods(["GET"])
def delete_answer(request, answer_pk):
	answer = Answer.objects.get(pk=answer_pk)
	answer.delete()
	return redirect('manage')


@require_http_methods(["GET"])
def delete_question(request, question_pk):
	question = Question.objects.get(pk=question_pk)
	question.delete()
	return redirect('manage')
