from django.db import models
from service._model.entity import Entity
from django.contrib.auth.models import User

class Process(models.Model):
    entity = models.ForeignKey(
        verbose_name="Ürün / Cihaz",
        to=Entity,
        on_delete=models.CASCADE,
    )

    implementation = models.TextField(
        verbose_name="Yapılan İşlem",
    )

    amount = models.DecimalField(
        verbose_name="Tutar (₺)",
        max_digits=10,
        decimal_places=2,
    )

    description = models.TextField(
        verbose_name="Açıklama",
        blank=True,
        null=True,
    )

    note = models.TextField(
        verbose_name="Not",
        blank=True,
        null=True,
    )

    edited = models.DateTimeField(
        verbose_name="Değiştirilme Tarih/Saat",
        auto_now=True,
    )

    created = models.DateTimeField(
        verbose_name="Oluşturulma Tarih/Saat",
        auto_now_add=True,
    )

    def __str__(self):
        return self.implementation

    class Meta:
        verbose_name="Yapılan İşlem"
        verbose_name_plural="Yapılan İşlemler"
