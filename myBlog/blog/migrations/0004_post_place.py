# Generated by Django 4.1.7 on 2023-03-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='place',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
