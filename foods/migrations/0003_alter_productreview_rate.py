# Generated by Django 3.2.6 on 2022-02-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_auto_20220205_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]