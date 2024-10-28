# Generated by Django 5.1.1 on 2024-09-29 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_bd_content_bd_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='bd',
            options={'ordering': ['-published'], 'verbose_name': 'Обявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterField(
            model_name='bd',
            name='content',
            field=models.TextField(default=' ', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публицации'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='bd',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.rubric', verbose_name='Рубрика'),
        ),
    ]