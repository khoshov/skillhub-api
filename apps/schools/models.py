from ckeditor.fields import RichTextField

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.fields import AutoSlugField


class School(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=255,
    )
    slug = AutoSlugField(
        _('Слаг'),
        populate_from='name',
        unique=True,
    )
    description = RichTextField(
        _('Описание'),
        blank=True, null=True,
    )
    accredited = models.BooleanField(
        _('Аккредитованное учебное заведение'),
        default=False,
    )
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

    def get_absolute_url(self):
        return reverse('api-1:get_school', kwargs={'slug': self.slug})


class SchoolAlias(models.Model):
    name = models.CharField(
        _('Имя'),
        max_length=255,
        unique=True,
    )
    school = models.ForeignKey(
        'schools.School',
        models.CASCADE,
        # related_name='aliases',
        verbose_name=_('Школа'),
    )

    class Meta:
        verbose_name = _('Псевдоним школы')
        verbose_name_plural = _('Псевдонимы школ')

    def __str__(self):
        return self.name
