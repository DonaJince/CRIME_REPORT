# Generated by Django 4.0.5 on 2022-10-19 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crime', '0011_blockchain_ledger_encripted_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blockchain_ledger',
            name='fir',
        ),
        migrations.RemoveField(
            model_name='blockchain_ledger',
            name='user',
        ),
        migrations.RemoveField(
            model_name='blockchain_ledger_encripted',
            name='fir',
        ),
        migrations.RemoveField(
            model_name='blockchain_ledger_encripted',
            name='user',
        ),
        migrations.RemoveField(
            model_name='fir',
            name='blockchain_count',
        ),
        migrations.RemoveField(
            model_name='fir',
            name='blockchain_entry_count',
        ),
        migrations.RemoveField(
            model_name='fir',
            name='blockchain_status',
        ),
        migrations.DeleteModel(
            name='Blockchain_admin',
        ),
        migrations.DeleteModel(
            name='Blockchain_ledger',
        ),
        migrations.DeleteModel(
            name='Blockchain_ledger_encripted',
        ),
    ]
