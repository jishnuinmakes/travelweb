# Generated by Django 4.2.6 on 2023-10-07 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_rename_ame_dp_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dp',
            old_name='desc',
            new_name='desc1',
        ),
        migrations.RenameField(
            model_name='dp',
            old_name='img',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='dp',
            old_name='name',
            new_name='name1',
        ),
    ]