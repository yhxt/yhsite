# Generated by Django 2.0.1 on 2018-01-22 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否已删除'),
        ),
    ]