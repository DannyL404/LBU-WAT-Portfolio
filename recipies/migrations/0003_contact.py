# Generated by Django 5.1.4 on 2025-01-16 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0002_recipies_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
