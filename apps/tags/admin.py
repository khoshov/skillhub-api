from django.contrib import admin

from apps.tags.models import Tag, TagOption


class TagOptionInline(admin.TabularInline):
    model = TagOption
    extra = 0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [TagOptionInline]
