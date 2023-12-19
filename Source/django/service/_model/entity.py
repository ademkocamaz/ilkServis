from django.db import models
from service._model.service import Service
from django.contrib.auth.models import User

class Entity(models.Model):
    service = models.ForeignKey(
        verbose_name="Servis Kaydı",
        to=Service,
        on_delete=models.CASCADE,
    )

    tag = models.CharField(
        verbose_name="Etiket",
        max_length=500,
        blank=True,
        null=True,
    )

    name = models.CharField(
        verbose_name="Adı",
        max_length=500,
    )

    location = models.CharField(
        verbose_name="Konum",
        max_length=500,
        blank=True,
        null=True,
    )

    status = models.CharField(
        verbose_name="Durum",
        max_length=500,
        blank=True,
        null=True,
    )

    manufacturer = models.CharField(
        verbose_name="Üretici",
        max_length=500,
        blank=True,
        null=True,
    )

    brand = models.CharField(
        verbose_name="Marka",
        max_length=500,
        blank=True,
        null=True,
    )

    model = models.CharField(
        verbose_name="Model",
        max_length=500,
        blank=True,
        null=True,
    )

    serial_number = models.CharField(
        verbose_name="Seri Numarası",
        max_length=500,
        blank=True,
        null=True,
    )

    product_number = models.CharField(
        verbose_name="Ürün Numarası",
        max_length=500,
        blank=True,
        null=True,
    )

    inventory_number = models.CharField(
        verbose_name="Stok Numarası",
        max_length=500,
        blank=True,
        null=True,
    )

    used_by = models.CharField(
        verbose_name="Kullanan Birim / Kullanıcı",
        max_length=500,
        blank=True,
        null=True,
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
        return self.name

    class Meta:
        verbose_name = "Ürün / Cihaz"
        verbose_name_plural = "Ürünler / Cihazlar"
