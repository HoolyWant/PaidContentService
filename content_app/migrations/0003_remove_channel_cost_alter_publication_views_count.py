# Generated by Django 4.2.8 on 2023-12-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0002_alter_channel_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='cost',
        ),
        migrations.AlterField(
            model_name='publication',
            name='views_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='кол-во просмотров'),
        ),
    ]
