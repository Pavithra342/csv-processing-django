# Generated by Django 5.1.5 on 2025-03-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
