# Generated by Django 4.0.2 on 2022-03-04 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apidemo', '0003_rename_post_articles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='content',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='title',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='Email',
        ),
    ]
