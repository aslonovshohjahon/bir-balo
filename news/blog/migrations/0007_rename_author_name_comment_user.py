# Generated by Django 5.0.1 on 2024-01-31 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_comment_comment_text_comment_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author_name',
            new_name='user',
        ),
    ]
