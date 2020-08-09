from django.contrib import admin
from .models import Spot, Theme
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.
class SpotAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
class ThemeAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Spot, SpotAdmin)
admin.site.register(Theme, ThemeAdmin)