# Generated by Django 4.0.2 on 2022-03-02 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apidemo', '0002_alter_post_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Articles',
        ),
    ]
