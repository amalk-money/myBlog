# Generated by Django 4.1.7 on 2023-03-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('query', models.CharField(max_length=500)),
            ],
        ),
    ]