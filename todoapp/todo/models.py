from django.db import models
from Userapp.models import User


class Project(models.Model):
    title = models.CharField(max_length=64, verbose_name='Проект')
    link = models.CharField(max_length=256, verbose_name='Ссылка')
    users = models.ManyToManyField(User, verbose_name='Пользователи работающие с проектом')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Todo(models.Model):
    text = models.CharField(max_length=256)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
