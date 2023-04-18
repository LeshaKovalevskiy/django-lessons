from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # print(request)
    return HttpResponse("Hello, world")


def test(request):
    return HttpResponse("<h1>Тестовая страница</h1>")
