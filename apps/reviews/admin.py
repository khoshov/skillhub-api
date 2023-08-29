from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from reviews.models import Review, ReviewSource, CriterionVariation, Criterion


class ReviewResource(resources.ModelResource):

    class Meta:
        model = Review
        exclude = ('source',)


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('id', 'url', 'rating', 'school', 'source', 'published')
    list_filter = ('school', 'rating', 'source', 'published')
    resource_class = ReviewResource


@admin.register(ReviewSource)
class ReviewSourceAdmin(admin.ModelAdmin):
    pass


class CriterionVariationInline(admin.TabularInline):
    model = CriterionVariation
    extra = 0


@admin.register(Criterion)
class CriterionAdmin(admin.ModelAdmin):
    inlines = [CriterionVariationInline]
