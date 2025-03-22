from django.contrib import admin
from service._model.entity import Entity
from service._admin.process import ProcessInline
from nested_admin.nested import NestedModelAdmin, NestedStackedInline


@admin.register(Entity)
class EntityAdmin(NestedModelAdmin):
    list_display = [field.name for field in Entity._meta.fields]
    list_display_links = [field.name for field in Entity._meta.fields]
    search_fields = [field.name for field in Entity._meta.fields]
    readonly_fields = [
        "service",
    ]

    save_on_top = True

    inlines = [
        ProcessInline,
    ]

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()


class EntityInline(NestedStackedInline):
    model = Entity
    extra = 0
    max_num = 100
    classes = ("collapse-entry",)
    inlines = [
        ProcessInline,
    ]
