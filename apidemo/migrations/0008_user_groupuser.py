# Generated by Django 4.0.2 on 2022-03-08 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apidemo', '0007_groupuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='GroupUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apidemo.groupuser'),
        ),
    ]
