from django.contrib import admin
from .models import Post, Tour
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.
class PostAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class TourAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Tour, TourAdmin)