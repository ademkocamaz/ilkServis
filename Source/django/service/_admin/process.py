from django.contrib import admin
from service._model.process import Process
from nested_admin.nested import NestedStackedInline

class ProcessInline(NestedStackedInline):
    model = Process
    extra = 0
    max_num = 100
    classes = ("collapse-entry",)