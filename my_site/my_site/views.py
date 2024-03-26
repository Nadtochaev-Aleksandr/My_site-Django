from django.shortcuts import render, HttpResponse # Необходимые импорты


def firstpage(request): # функция представления firstpage. Содержит обязательный аргумент request - информацию о запросе
    return render(request, "html/firstpage.html") # функция firstpage возвращает функцию render, которой первым аргументом передан request (обязательный аргумент!!!), а вторым аргументом передан путь к файлу html шаблона (html/firstpage.html) - Обязательный аргумент. Следовательно при отработке функции представления firstpage будет отработан html шаблон firstpage.html, располагающийся по пути my_site/templates/html/firstpage.html

