# Generated by Django 3.1.4 on 2020-12-05 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201205_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='middle_name',
        ),
    ]
