# Generated by Django 3.1.1 on 2020-09-25 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200925_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='challenge',
            new_name='challenge_id',
        ),
        migrations.RenameField(
            model_name='mentor',
            old_name='user',
            new_name='user_id',
        ),
    ]