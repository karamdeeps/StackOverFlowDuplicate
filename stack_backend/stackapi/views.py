
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from bs4 import BeautifulSoup
from rest_framework import viewsets
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question
from .serializer import QuestionSerializer


def index(request):
    question_list = Question.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(question_list, 10)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'questions': questions})
    # return render(request, 'index.html')


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


def fetch_questions(request):
    try:
        res = requests.get("https://stackoverflow.com/questions")
        soup = BeautifulSoup(res.text, "html.parser")
        questions_data = {
            "questions": []
        }
        questions = soup.select(".question-summary")
        for que in questions:
            q = que.select_one('.question-hyperlink').getText()
            vote_count = que.select_one('.vote-count-post').getText()
            views = que.select_one('.views').attrs['title']
            tags = [i.getText() for i in (que.select('.post-tag'))]

            Question.objects.create(
                question=q,
                vote_count=vote_count,
                views=views,
                tags=tags
            )
        return HttpResponse("Latest Data Fetched From StackOverFlow")

    except Exception as error:
        print(error)
        return HttpResponse("FAILED TO FETCH QUESTIONS")


def list(request):
    question_list = Question.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(question_list, 10)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'questions': questions})
