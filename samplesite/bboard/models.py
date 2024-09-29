from django.db import models


class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(default=' ', verbose_name='Описание')
    price = models.FloatField(default=0.0, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Дата публицации')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,
                               verbose_name='Рубрика')


    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Обявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True,
                            verbose_name='Название')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

