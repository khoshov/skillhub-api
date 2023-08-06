# Generated by Django 4.2.4 on 2023-08-02 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reviews', '0001_initial'),
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Метка',
                'verbose_name_plural': 'Метки',
            },
        ),
        migrations.CreateModel(
            name='TagOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='tags.tag', verbose_name='Метка')),
            ],
            options={
                'verbose_name': 'Вариант метки',
                'verbose_name_plural': 'Варианты меток',
            },
        ),
        migrations.CreateModel(
            name='TagMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.review', verbose_name='Отзыв')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.school', verbose_name='Школа')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.tag', verbose_name='Метка')),
            ],
            options={
                'verbose_name': 'Совпадение метки',
                'verbose_name_plural': 'Совпадения меток',
            },
        ),
    ]