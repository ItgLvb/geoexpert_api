from django.db import models


class CadastralPlot(models.Model):
    cadastral_number = models.CharField(
        'Кадастровый номер',
        max_length=25,
        unique=True
    )
    short_cadastral_number = models.CharField(
        'Короткий кадастровый номер',
        max_length=20,
        blank=True,
        null=True,
    )
    geometry = models.TextField(
        'Геометрия участка'
    )
    address = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        if self.cadastral_number:
            return self.cadastral_number
        else:
            return self.short_cadastral_number
        
    class Meta:
        verbose_name = 'Кадастровые участок'
        verbose_name_plural = 'Кадастровый участки'
