from django.contrib import admin
from .models import Actor, Drama, Group, Show, Showman, Singer
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.
class ActorAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
class DramaAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
class GroupAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
class ShowAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
class ShowmanAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
class SingerAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Actor, ActorAdmin)
admin.site.register(Drama, DramaAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Showman, ShowmanAdmin)
admin.site.register(Singer, SingerAdmin)