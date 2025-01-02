from django.contrib import admin
from service._model.service import Service
from service._admin.entity import EntityInline
from django_object_actions import DjangoObjectActions, action
from service._model.entity import Entity


@admin.register(Service)
class ServiceAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]
    list_display_links = [field.name for field in Service._meta.fields]
    search_fields = [field.name for field in Service._meta.fields]
    readonly_fields = [
        "user",
    ]

    save_on_top = True
    save_as_continue = False

    inlines = [
        EntityInline,
    ]

    """ @action(label="Yazdır", description="Seçili kaydı yazdırır.")
    def print(self, request, obj):
        service = obj
        entities = Entity.objects.filter(service=service)
        processes=[]
        for entity in entities:
            processes.append() 
    change_actions = ("print",)
    # changelist_actions = ('print', ) """

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()

    
