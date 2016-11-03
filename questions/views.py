from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Question, Answer, Quiz, Statistic
from .forms import QuestionForm, AnswerForm
import signals


# Create your views here.

def manage(request, quiz_pk):
    quest = Question()
    ans = Answer()
    quiz = Quiz.objects.get(pk=quiz_pk)
    
    questions = []
    for question in Question.objects.filter(quiz=quiz):
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
                return redirect('manage', quiz_pk=quiz_pk)
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
                statistics = Statistic.objects.create()
                Question.objects.create(question=question, quiz=quiz, statistics=statistics)

                return redirect('manage', quiz_pk=quiz_pk)
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
            "quiz_pk": quiz_pk,
            'name': quiz.name,
            })

def end_page(request, right, total, quiz_pk):
	quiz = Quiz.objects.get(pk=quiz_pk)
	return render(request, 'questions/end_page.html',
                    {'right': right,
                    'total': total,
                    'name': quiz.name,
                    'pk': quiz_pk,
                    })

def start(request, quiz_pk):
    quiz = Quiz.objects.get(pk=quiz_pk)
    questions = []
    for question in Question.objects.filter(count__gte=1, quiz=quiz):
        questions.append((question,question.answers.filter()))
    if len(questions) < 2:
        return render(request, 'questions/error.html')
    return render(request, 'questions/start.html',
        {
        'quiz': Quiz.objects.get(pk=quiz_pk)
        })

def reset(request, quiz_pk):
    quiz = Quiz.objects.get(pk=quiz_pk)
    questions = Question.objects.filter(quiz=quiz)
    for question in questions:
        question.statistics.total = 0
        question.statistics.right = 0
        question.statistics.save()

    return redirect('manage', quiz_pk=quiz_pk)

def questions(request, quiz_pk):
    questions = []
    quiz = Quiz.objects.get(pk=quiz_pk)
    for question in Question.objects.filter(count__gte=1, quiz=quiz):
        questions.append((question,question.answers.filter()))


    if request.method == "POST":
        right_count= 0
        total = len(Question.objects.filter(count__gte=1, quiz=quiz))

        for question in Question.objects.filter(count__gte=1, quiz=quiz):
            user_answer = request.POST.get('answer-on-' + str(question.pk))
            right_ans = Answer.objects.filter(question=question, is_Correct=True)
            if right_ans:
            	right_answer = right_ans[0].answer
            else:
            	right_answer = ''
            if right_answer == user_answer:
                right_count += 1
                question.statistics.right += 1
            question.statistics.total += 1
            question.statistics.save()

    	return redirect('end_page', right=right_count, total=total, quiz_pk=quiz_pk)
        
    else:
        return render(request, 'questions/quiz.html',
                        {'questions': questions,
                        })



@require_http_methods(["GET"])
def make_right(request, answer_pk, question_pk, quiz_pk):
    question = Question.objects.get(pk=question_pk)
    answers = Answer.objects.filter(question=question)
    for answer in answers:
        answer.is_Correct = False
        answer.save()
	answer = Answer.objects.get(pk=answer_pk)
	answer.is_Correct = True
	answer.save()
    return redirect('manage', quiz_pk=quiz_pk)


@require_http_methods(["GET"])
def delete_answer(request, answer_pk):
	answer = Answer.objects.get(pk=answer_pk)
	answer.delete()
	return redirect('manage')


@require_http_methods(["GET"])
def delete_question(request, question_pk, quiz_pk):
	question = Question.objects.get(pk=question_pk)
	question.delete()
	return redirect('manage', quiz_pk=quiz_pk)

def main(request):

	return render(request, 'questions/main.html',
                        {'quizes': Quiz.objects.all(),
                        })