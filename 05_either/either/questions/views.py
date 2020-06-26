from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer
# Create your views here.
# get_object_or_404: object를 가지고 오거나, 404에러를 내거나,

def index(request):
    return render(request, 'questions/index.html')

def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('questions:detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form' : form
    }
    return render(request, 'questions/form.html', context)

def detail(request, question_pk):
    #question = Question.objects.get(pk=question_pk)
    question = get_object_or_404(Question, pk=question_pk)
    answers = question.answer_set.all()
    answer_a = answers.filter(choice='a').count()
    answer_b = len(answers.filter(choice='b'))
    # 모델이름, pk이름을 적어주면 된다.
    # pk 조회 시 pk 값이 없다면 404 에러를 보여줌
    answer_form = AnswerForm
    
    context = {
        'question': question,
        'answer_form': answer_form,
        'answer_a': answer_a,
        'answer_b': answer_b,
    }
    return render(request, 'questions/detail.html', context)

def answer_create(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.user = request.user
        answer.question = question
        answer.save()
        return redirect('questions:detail', question_pk)
