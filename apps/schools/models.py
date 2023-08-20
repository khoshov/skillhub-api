from ckeditor.fields import RichTextField

from django.db import models
from django.utils.translation import gettext_lazy as _


class School(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=255,
    )
    description = RichTextField(
        _('Описание'),
        blank=True, null=True,
    )
    accredited = models.BooleanField(
        _('Аккредитованное учебное заведение'),
        default=False,
    )
    # TODO: Переделать на cached property
    # rating = models.FloatField(
    #     _('Рейтинг'),
    #     default=0,
    # )
    epc = models.FloatField(
        _('Средний заработок с перехода'),
        default=0
    )
    is_active = models.BooleanField(
        _('Активный'),
        default=False,
    )

    meta_title = models.CharField(
        _('Meta title'),
        max_length=255,
        blank=True, null=True,
    )
    meta_description = models.TextField(
        _('Meta description'),
        blank=True, null=True,
    )

    class Meta:
        db_table = 'school'
        verbose_name = _('Школа')
        verbose_name_plural = _('Школы')

    def __str__(self):
        return self.name


class SchoolAlias(models.Model):
    name = models.CharField(
        _('Имя'),
        max_length=255,
        unique=True,
    )
    school = models.ForeignKey(
        'schools.School',
        models.CASCADE,
        related_name='aliases',
        verbose_name=_('Школа'),
    )

    class Meta:
        verbose_name = _('Псевдоним школы')
        verbose_name_plural = _('Псевдонимы школ')

    def __str__(self):
        return self.name


class SchoolTag(models.Model):
    name = models.CharField(
        _('Имя'),
        max_length=255,
    )

    class Meta:
        verbose_name = _('Метка')
        verbose_name_plural = _('Метки')

    def __str__(self):
        return self.name


class SchoolTagOption(models.Model):
    text = models.TextField(
        _('Текст'),
    )
    tag = models.ForeignKey(
        'schools.SchoolTag',
        models.CASCADE,
        related_name='options',
        verbose_name=_('Метка'),
    )

    class Meta:
        verbose_name = _('Вариант метки')
        verbose_name_plural = _('Варианты меток')

    def __str__(self):
        return self.text
