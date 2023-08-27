from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
    MISSING = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    STARS = (
        (MISSING, _('Нет рейтинга')),
        (ONE, _('Одна звезда')),
        (TWO, _('Две звезды')),
        (THREE, _('Три звезды')),
        (FOUR, _('Четыре звезды')),
        (FIVE, _('Пять звёзд')),
    )

    UNKNOWN = 1
    NEGATIVE = 2
    NEUTRAL = 3
    POSITIVE = 4

    SENTIMENT = (
        (UNKNOWN, _('Неизвестен')),
        (NEGATIVE, _('Негативный')),
        (NEUTRAL, _('Нейтральный')),
        (POSITIVE, _('Позитивный')),
    )

    school = models.ForeignKey(
        'schools.School',
        models.CASCADE,
        related_name='reviews',
        verbose_name=_('Школа'),
    )
    source = models.ForeignKey(
        'reviews.ReviewSource',
        models.CASCADE,
        verbose_name=_('Источник отзыва'),
        blank=True, null=True,
    )
    url = models.URLField(
        _('Ссылка на отзыв'),
    )
    published = models.DateField(
        _('Дата публикации отзыва'),
    )
    rating = models.IntegerField(
        _('Рейтинг'),
        choices=STARS,
        default=MISSING,
    )
    advantages = models.TextField(
        _('Положительная часть отзыва'),
        blank=True, null=True,
    )
    disadvantages = models.TextField(
        _('Отрицательная часть отзыва'),
        blank=True, null=True,
    )
    text = models.TextField(
        _('Основной текст отзыва'),
        blank=True, null=True,
    )
    text_sentiment = models.IntegerField(
        _('Тональность текста отзыва'),
        choices=SENTIMENT,
        default=UNKNOWN,
    )

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __str__(self):
        return self.url


class ReviewSource(models.Model):
    name = models.CharField(
        _('Источник отзыва'),
        max_length=255,
    )
    description = RichTextField(
        _('Дополнительный текст'),
        blank=True, null=True,
    )

    class Meta:
        verbose_name = _('Источник отзывов')
        verbose_name_plural = _('Источники отзывов')

    def __str__(self):
        return self.name


class ReviewTagMatch(models.Model):
    review = models.ForeignKey(
        'reviews.Review',
        models.CASCADE,
        related_name='matches',
        verbose_name=_('Отзыв'),
    )
    tag_option = models.ForeignKey(
        'schools.SchoolTagOption',
        models.CASCADE,
        verbose_name=_('Вариант метки'),
    )
    text = models.TextField(
        _('Текст'),
    )

    class Meta:
        verbose_name = _('Совпадение метки')
        verbose_name_plural = _('Совпадения меток')

    def __str__(self):
        return self.text
