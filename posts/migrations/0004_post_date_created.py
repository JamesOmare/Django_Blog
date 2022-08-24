# Generated by Django 4.1 on 2022-08-17 07:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
