# Generated by Django 3.2 on 2021-05-24 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0006_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=255, null=True),
        ),
    ]