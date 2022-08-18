from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(verbose_name="Название услуги", max_length=32, unique=True, blank=False)
    price = models.PositiveIntegerField(verbose_name="Цена услуги", blank=False)
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Время обновления публикации", auto_now=True)

    class Meta:
        verbose_name_plural = "Услуги"
        verbose_name = "Услуга"

    def __str__(self):
        return f'{self.title} | {self.price}'


