# Generated by Django 4.2.8 on 2023-12-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0003_remove_channel_cost_alter_publication_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='views_count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='кол-во просмотров'),
        ),
    ]
