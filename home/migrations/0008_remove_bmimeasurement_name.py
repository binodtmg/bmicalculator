# Generated by Django 3.2 on 2021-05-22 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_bmimeasurement_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmimeasurement',
            name='name',
        ),
    ]