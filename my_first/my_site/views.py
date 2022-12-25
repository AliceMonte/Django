from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Главная</h1>")
def about(request):
    return HttpResponse("<h2>О Нас</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def user(request, user, age ='29'):
    return HttpResponse(f"<h2>Имя: {user}, Возраст: {age}</h2>")