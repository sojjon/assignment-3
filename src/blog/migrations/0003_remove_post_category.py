# Generated by Django 4.2.1 on 2023-05-20 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_category_post_content_post_featured_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]