from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    date = models.DateTimeField(
        verbose_name="Tarih / Saat",
    )

    customer = models.CharField(
        verbose_name="Müşteri / Firma Bilgileri",
        max_length=500,
    )

    phone1 = models.CharField(
        verbose_name="Telefon-1",
        max_length=500,
        blank=True,
        null=True,
    )

    phone2 = models.CharField(
        verbose_name="Telefon-2",
        max_length=500,
        blank=True,
        null=True,
    )

    address=models.TextField(
        verbose_name="Adres",
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

    user = models.ForeignKey(
        verbose_name="Düzenleyen Kullanıcı",
        to=User,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name = "Servis Kaydı"
        verbose_name_plural = "Servis Kayıtları"
