# Generated by Django 4.0.2 on 2022-03-17 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apidemo', '0010_group_remove_groupuser_groupcode_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='GroupCode',
        ),
    ]
