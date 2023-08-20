# Generated by Django 4.2.4 on 2023-08-20 17:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Ссылка на отзыв')),
                ('published', models.DateField(verbose_name='Дата публикации отзыва')),
                ('rating', models.IntegerField(choices=[(0, 'Нет рейтинга'), (1, 'Одна звезда'), (2, 'Две звезды'), (3, 'Три звезды'), (4, 'Четыре звезды'), (5, 'Пять звёзд')], default=0, verbose_name='Рейтинг')),
                ('advantages', models.TextField(blank=True, null=True, verbose_name='Положительная часть отзыва')),
                ('disadvantages', models.TextField(blank=True, null=True, verbose_name='Отрицательная часть отзыва')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Основной текст отзыва')),
                ('text_sentiment', models.IntegerField(choices=[(1, 'Неизвестен'), (2, 'Негативный'), (3, 'Нейтральный'), (4, 'Позитивный')], default=1, verbose_name='Тональность текста отзыва')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='schools.school', verbose_name='Школа')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='ReviewSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Источник отзыва')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Дополнительный текст')),
            ],
            options={
                'verbose_name': 'Источник отзывов',
                'verbose_name_plural': 'Источники отзывов',
            },
        ),
        migrations.CreateModel(
            name='ReviewTagMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='reviews.review', verbose_name='Отзыв')),
                ('tag_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.schooltagoption', verbose_name='Вариант метки')),
            ],
            options={
                'verbose_name': 'Совпадение метки',
                'verbose_name_plural': 'Совпадения меток',
            },
        ),
        migrations.AddField(
            model_name='review',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.reviewsource', verbose_name='Источник отзыва'),
        ),
    ]
