# Generated by Django 5.1.2 on 2024-11-14 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_categories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostInCategory',
        ),
    ]