from django.db import models
from django.urls import reverse

class Library (models.Model):

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("library")
        verbose_name_plural = ("libraries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("library _detail", kwargs={"pk": self.pk})