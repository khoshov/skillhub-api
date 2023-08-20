from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from core.admin import activate, deactivate

from schools.models import School, SchoolAlias, SchoolTag, SchoolTagOption


class SchoolResource(resources.ModelResource):
    class Meta:
        model = School


class SchoolAliasInline(admin.TabularInline):
    model = SchoolAlias
    extra = 0


@admin.register(School)
class SchoolAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_filter = ('is_active',)
    inlines = [SchoolAliasInline]
    actions = [activate, deactivate]


class TagOptionInline(admin.TabularInline):
    model = SchoolTagOption
    extra = 0


@admin.register(SchoolTag)
class TagAdmin(admin.ModelAdmin):
    inlines = [TagOptionInline]
