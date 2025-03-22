from django.contrib import admin
from service._model.service import Service
from service._model.entity import Entity
from service._model.process import Process

from service._admin.entity import EntityInline

from django_object_actions import DjangoObjectActions, action
from django.shortcuts import render
from nested_admin.nested import NestedModelAdmin

import json
from django.core.serializers import serialize


@admin.register(Service)
class ServiceAdmin(DjangoObjectActions, NestedModelAdmin):
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

    @action(label="Yazdır", description="Seçili kaydı yazdırır.")
    def print(self, request, obj):

        # service={"service":obj}
        service = serialize(
            "python",
            [
                obj,
            ],
        )
        # print(service)
        entities = serialize("python", Entity.objects.filter(service=obj))
        # print(entities)
        total = 0
        for entity in entities:
            processes = serialize("python", Process.objects.filter(entity=entity["pk"]))
            amount = 0
            for process in processes:
                amount += process["fields"]["amount"]

            entity["processes"] = processes
            entity["amount"] = amount
            # print(entity)
            total += amount
        service[0]["total"] = total
        context = {
            "service": service[0],
            "entities": entities,
        }
        return render(
            request=request, template_name="service_print.html", context=context
        )

    change_actions = ("print",)
    # changelist_actions = ('print', )

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()
