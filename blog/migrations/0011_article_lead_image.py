# Generated by Django 3.1.2 on 2021-02-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210131_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='lead_image',
            field=models.ImageField(default='no_image.png', upload_to='images'),
        ),
    ]