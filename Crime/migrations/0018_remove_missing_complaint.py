# Generated by Django 4.0.5 on 2022-10-19 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crime', '0017_missing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missing',
            name='complaint',
        ),
    ]
