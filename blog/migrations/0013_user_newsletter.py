# Generated by Django 3.1.2 on 2021-02-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_user_is_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='newsletter',
            field=models.BooleanField(default=False),
        ),
    ]
