from django.shortcuts import render, redirect
from .models import Question, Choice

def index(request):
    request.session['score'] = 0
    request.session['question_amount'] = Question.objects.all().count()
    return render(request, 'index.html')

def question(request, question_number):
    question = Question.objects.get(number=question_number)
    context = {
        'question': question
    }
    return render(request, 'question.html', context)

def submit_choice(request, question_number):
    question = Question.objects.get(number=question_number)
    choice = Choice.objects.get(id=request.POST['choice_id'])
    if choice.is_correct:
        request.session['score'] = request.session['score'] + 1
    if question.number == request.session['question_amount']:
        return redirect('/total')
    return redirect(f'/questions/{question.number + 1}')

def total(request):
    return render(request, 'total.html')