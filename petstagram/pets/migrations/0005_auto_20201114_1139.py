# Generated by Django 3.1.1 on 2020-11-14 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_auto_20201114_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='image_url',
            new_name='image',
        ),
    ]
