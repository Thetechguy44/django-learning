# Generated by Django 5.1 on 2024-08-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_country', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('course', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
