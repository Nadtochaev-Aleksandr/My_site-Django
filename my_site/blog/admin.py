from django.contrib import admin
from .models import *

class EducationAdmin(admin.ModelAdmin): # Класс для тонкой настройки приложения блог в админ панели
    list_display = ('id', 'name', 'start', 'finish', 'speciality', 'qualification') # переменная List_display содержит в себе наименование полей, которые надо отображать для модели Education в админ панели


admin.site.register(Education, EducationAdmin) # регистрация модели Education, для того чтобы с ней можно было работать в админ панели. Вторым перементром передан недавно созданный класс EducationAdmin - для тонкой настройки пользования моделью Education через админ панель.

admin.site.register(Experience)  # регистрация модели Experience, для того чтобы с ней можно было работать в админ панели.
admin.site.register(ProfScills)  # регистрация модели ProfScills, для того чтобы с ней можно было работать в админ панели.
admin.site.register(PersonalScills)  # регистрация модели PersonalScills, для того чтобы с ней можно было работать в админ панели.
admin.site.register(PersonalInfo)  # регистрация модели PersonalInfo, для того чтобы с ней можно было работать в админ панели.