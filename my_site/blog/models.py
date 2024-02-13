from django.db import models

# Create your models here.
class Education(models.Model):
    name=models.CharField(verbose_name='Наименование учебного заведения', max_length=250)
    start=models.DateField(verbose_name='Дата начала оббучения')
    finish = models.DateField(verbose_name='Дата завершения оббучения')
    speciality = models.CharField(verbose_name='Специальность', max_length=250)
    qualification = models.CharField(verbose_name='Квалификация', max_length=250)
    bal = models.CharField(verbose_name='Средний балл', max_length=5)
    notification = models.TextField(verbose_name='Примечание', null=True, blank=True)