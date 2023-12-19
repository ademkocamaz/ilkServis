from django.contrib import admin
from service._model.process import Process


class ProcessInline(admin.StackedInline):
    model = Process
    extra = 0
    max_num = 100
    classes = ("collapse-entry",)