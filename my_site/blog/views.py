from django.shortcuts import render, HttpResponse # необходимые импорты
from .models import * # из models приложения blog импортируются все модели (* = все)

def blog1(request): # Это надо передалеать!!! функция представления blog1. Содержит в себе обязательный параметра request, содержащий информацию о запросе
    info=Blog.objects.all() # переменная info, которой присвоены все элементы модели Blog (объект queryset)
    return render(request, 'blog/html/blog1.html', {"list":info}) #воврат фукнции render, которая принимает в себя request (первый аргумент - обязательный!!!), путь к функции представления blog1 как 'blog/html/blog1.html' (второй аргумент - обязательный!!!), и третий (необязательный аргумент) context в виде словаря {"list":info} где ключ словаря "list" будет отображаться в шаблоне на который ссылается функция blog1, а значение этого ключа info будут выведены пользователю при отработке шаблона

def education(request): # функция представления education. Содержит в себе обязательный параметра request, содержащий информацию о запросе
    educations=Education.objects.all() # переменная educations, которой присвоены все элементы модели Education (объект queryset)
    context ={'university':educations} # Переменная context, которой задан соварь, чтобы потом подставить его третим аргментеом в функцию render
    return render(request, 'blog/html/blog2.html', context) # возврат функции render, содержащей первым аргументом request - информацию о запросе (Обязательный аргумент!!!), вторым аргументом - путь к функции представления blog2 как строка 'blog/html/blog2.html' (обязательный аргумент), и третим аргументом передан context, как переменная, заданная строкой ранее.

def education_detail(request, pk): # Функция представления education_detail, которой передан обязательный аргумент request и вторым аргументом передан pk - это параметр, отлавливаемый в функции path файла urls.py для данной функции представления через параментр строки запроса
    education=Education.objects.get(pk=pk) #определяется переменная education, которой передается всё объекты модели Education в которой id = pk - т.е. всё для конкретного поста. Объект queryset
    context = {'university': education} # Задаеётся переменная context, которая потом будет передана третьим аргументом в функцию render. Данно переменной передан словарь с ключем 'university' и значением для данного ключа в виде переменной education, определенной строкой выше
    return render(request, 'blog/html/blog2_detail.html', context) #Возврат функции render (шаблонизатора django), которой в свою очередь первым аргументом передан request (обязательный аргумент). Вторым аргументом передан путь к html шаблону blog2_detail ('blog/html/blog2_detail.html'). Третьим аргументом передана переменная context.

def experience(request): # Функция представления experience, которой передан обязательный аргумент request, содержащий информацию о запросе
    experiences=Experience.objects.all() # задана переменная experiences, которой переданы все объекты модели Experience (объект queryset)
    context ={'jobs': experiences } # Задана переменная context, которой передан словарь с ключем 'jobs' и значением равном переменной experiences, определенной строкой выше. Данная переменная context, будет передана третим аргументом в функцию render. Ключь словаря "jobs" можно будет подставлять в html шаблоны, а при отработке данного шаблона будет выведены данные соответсвующие значению словаря по данному ключу - experiences
    return render(request, 'blog/html/blog3_experience.html', context) #возврат функции render (шаблонизатора django), которой первым аргументом передан request, вторым - путь к html файлу шаблону blog3_experience.html ('blog/html/blog3_experience.html'). Третьим аргументом передана переменная context, определленная строкой ранее.

def experience_detail(request, pk): # Функция представления experience_detail, которой передан request (обязательный параметр) и параметра pk, приходящий к нам из url. В зависимости от значения данного параметра будут выводиться те или иные данные
    experience=Experience.objects.get(pk=pk) # переменная которая оперделена как все объекты модели Experience у которых id=pk (объект queryset)
    context ={'job': experience } # определена переменная context, которой передан словарь с ключем job и значениме experience - переменной, определенной строкой ранее
    return render(request, 'blog/html/blog3_detail.html', context) # возврат функции render (шаблонизатора django), которой первым параметром передан request, вторым - путь к html файлу с шаблоном - 'blog/html/blog3_detail.html', третьим - ранее определенная переменная context для передачи данных в шаблон

def profscills(request): # Функция представления profscills, которой передан аргумент request
    scills=ProfScills.objects.all() # Определена переменная scills которой переданы все объекты модели ProfScills (объект queryset)
    context = {'profscills':scills} # Опеределена переменная context, которой передан некий ключ profscills со значениями из переменной scills, опеределенной строкой ранее.
    return render(request, 'blog/html/blog4_profscills.html', context) # Возврат функции render (шаблонизатора django), которой первым аргументом передан request, вторым аргументом - путь к html файлу шаблона ('blog/html/blog4_profscills.html'), третьим - переменная context, определенная строкой выше - для передачи данных в шаблон

def personalscills(request): # Функция представления personalscills, которой передан аргумент request
    personscils=PersonalScills.objects.all() # определена переменная personalscills которой переданы все объекты модели PersonalScills (объект queryset)
    context={'personalscills':personscils} # Определена переменная context, которой переданы словарь с ключер personalscills и значениями по данному ключу равными personalscills - переменной, определенной строкой ранее.
    return render(request, 'blog/html/blog5_personalscills.html', context) # Возврат функции render - шаблонизатора django, которой первым аргументом передан request, вторым - путь к html файлу шаблона blog5_personalscills.html ('blog/html/blog5_personalscills.html'), третьим - переменная context, определенная строкой ранее, для передачи в шаблон данных

def personalinfo(request): # функуия представвления personalinfo, которой передан аргумент request
    info=PersonalInfo.objects.all() # Переменная info, которой переданы все объекты модели PersonalInfo, объект queryset
    context={ 'info': info, 'a':1 } # Определена переменная context, которая потом будет передана третьим аргументом функции render. Переменной context задан словарь в котором ключь определен как строка "pinfo", а значения по данному ключу есть переменная info, определенная строкой ранее.
    return render(request, 'blog/html/blog6_personalinfo.html', context) # возврат функции render (шаблонизатора django), которой первым аргументом передан request, вторым - путь к html фалу blog6_personalinfo.html ('blog/html/blog6_personalinfo.html'), а третьим - переменная context, заданная строкой ранее.