from django.db import models


class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(default=' ', verbose_name='Описание')
    price = models.FloatField(default=0.0, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Дата публицации')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Обявление'
        ordering = ['-published']


