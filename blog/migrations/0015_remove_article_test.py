# Generated by Django 3.1.6 on 2021-02-07 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_article_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='test',
        ),
    ]