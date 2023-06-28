# Generated by Django 3.2.18 on 2023-06-27 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastralplot',
            options={'verbose_name': 'Кадастровые участок', 'verbose_name_plural': 'Кадастровый участки'},
        ),
        migrations.AlterField(
            model_name='cadastralplot',
            name='cadastral_number',
            field=models.CharField(max_length=25, unique=True, verbose_name='Кадастровый номер'),
        ),
    ]