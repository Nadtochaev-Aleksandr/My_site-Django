"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Импорт admin для руководства админ панелью и ссылки на него при указании соотвествующейго url адреса admin
from django.urls import path, include # Необходимый импорт функции path, сюда же я добавил функцию include чтобы использовать ей на странице
from . import views # импорт файла views.py из папки в которой находится данный файл urls.py (т.е. my_site/views.py)

urlpatterns = [ # Переменная urlpatterns содержит в себе список функций path. Функция path - "Путь/след" отвечает за то какая функция представления будет отрабаотывать по какому url путм, принимает в себя имя url адреса, путь к функции представления и иные необязательные аргументы, например name
    path('admin/', admin.site.urls), # первая функция path, содержит адрес 'admin/' - переход на административную страницу сайта (первый атрибут, обязательный!!!) вторым атрибутом вместо классического адреса на функцию представления которая должна отработать при попадании на данный адрес представлена ссылка на класс, управляющйи админ панелью.
    path('blog/', include('blog.urls'), name='blog'), # вторая функция path. Содержаит адрес 'blog/'. Вторым аргументом вместо пути к функции представления передана фукнция include, которой в свою очередь передан путь к файлу urls.py приложения blog ('blog.urls'). Следовательно тут происходит перенаправление на url приложения blog. Т.е. попадая на адрес blog пользовательль будет пренаправлен на urls.py приложения blog
    path('portfolio/', include('portfolio.urls'), name='portfolio'), # третья функция path. Содержаит адрес 'portfolio/'. Вторым аргументом вместо пути к функции представления передана фукнция include, которой в свою очередь передан путь к файлу urls.py приложения portfolio ('portfolio.urls'). Следовательно тут происходит перенаправление на url приложения portfolio. Т.е. попадая на адрес portfolio пользовательль будет пренаправлен на urls.py приложения portfolio
    path('', views.firstpage, name='main') # четвертая функция path. Содержит адрес в виде пустой строки (" "). Следовательно пользователь ещё ничего не введя автоматически пападает на эту страницу. Так называемая главная страница. Вторым аргументом передан путь к функции firstpage файла views.py (views.firstpage). Третим аргументом задан аргумент name, определяющий имя url адреса, по которому на него можно будет ссылаться в шаблонах
]
