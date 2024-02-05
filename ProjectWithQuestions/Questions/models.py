from django.db import models


class Question(models.Model):
    division = models.CharField(max_length=150, verbose_name="Дивизион")
    company = models.CharField(max_length=150, verbose_name="Предприятие")
    text = models.TextField(verbose_name='Вопрос')
    email = models.EmailField(verbose_name='Электронная почта', blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
