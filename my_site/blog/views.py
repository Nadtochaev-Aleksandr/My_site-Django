from django.shortcuts import render, HttpResponse # необходимые импорты
from .models import * # из models приложения blog импортируются все модели (* = все)

def blog1(request): # Это надо передалеать!!! функция представления blog1. Содержит в себе обязательный параметра request, содержащий информацию о запросе
    info=Blog.objects.all() # переменная info, которой присвоены все элементы модели Blog (объект queryset)
    return render(request, 'blog/html/blog1.html', {"list":info}) #воврат фукнции render, которая принимает в себя request (первый аргумент - обязательный!!!), путь к функции представления blog1 как 'blog/html/blog1.html' (второй аргумент - обязательный!!!), и третий (необязательный аргумент) context в виде словаря {"list":info} где ключ словаря "list" будет отображаться в шаблоне на который ссылается функция blog1, а значение этого ключа info будут выведены пользователю при отработке шаблона

def education(request): # функция представления education. Содержит в себе обязательный параметра request, содержащий информацию о запросе
    educations=Education.objects.all() # переменная educations, которой присвоены все элементы модели Education (объект queryset)
    context ={'university':educations} # Переменная context, которой задан соварь, чтобы потом подставить его третим аргментеом в функцию render
    return render(request, 'blog/html/blog2.html', context) # возврат функции render, содержащей первым аргументом request - информацию о запросе (Обязательный аргумент!!!), вторым аргументом - путь к функции представления blog2 как строка 'blog/html/blog2.html' (обязательный аргумент), и третим аргументом передан context, как переменная, заданная строкой ранее.