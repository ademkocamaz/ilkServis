from django.contrib import admin
from service._model.service import Service
from service._admin.entity import EntityInline
from service._admin.process import ProcessInline

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]
    list_display_links = [field.name for field in Service._meta.fields]
    search_fields = [field.name for field in Service._meta.fields]
    readonly_fields = [
        "user",
    ]

    save_on_top = True

    inlines=[
        EntityInline,
    ]

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()
