# Generated by Django 5.0.1 on 2024-02-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0, verbose_name="Ko'rilgan"),
        ),
    ]
