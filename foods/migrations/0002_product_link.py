# Generated by Django 3.2.6 on 2021-12-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
