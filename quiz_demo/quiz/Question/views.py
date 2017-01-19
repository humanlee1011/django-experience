# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from User.models import User
from Question.models import Question, Answer
# Create your views here.

def question_info(request):
    if request.session.get('user_name', None):
        user = User.objects.get(user_name = request.session['user_name'])
        id = request.GET.get('id', None)

        if id != None:
            question = Question.objects.get(id = id)
            if request.method == 'POST':
                answer_content = request.POST.get('answer', None)
                answer = Answer.objects.create(author = user, question = question, content = answer_content)
                answer.save()
                question.number_of_answer += 1
                question.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                info = {'question': question, 'user': user}
                return render(request, 'Question/question_info.html', info)
    else:
        return HttpResponse('error')

def ask_question(request):
    if request.session.get('user_name', None):
        user = User.objects.get(user_name = request.session['user_name'])
        if request.method == 'POST':
            question_content = request.POST.get('question_content', None)
            if question_content != None:
                question = Question.objects.create(author = user, question_text = question_content)
                question.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("error: 问题不能为空！")
        else:
            info = {'user': user}
            return render(request, 'Question/ask_question.html', info)
    else:
        return HttpResponseRedirect(reverse('login'))
