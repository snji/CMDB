# Generated by Django 3.1.4 on 2020-12-23 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhost', '0002_auto_20201222_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='istrubiton',
            new_name='os_distrubiton',
        ),
    ]
