# Generated by Django 3.2.8 on 2023-07-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivra', '0003_auto_20230713_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='stuff',
            field=models.ManyToManyField(to='delivra.Product'),
        ),
    ]
