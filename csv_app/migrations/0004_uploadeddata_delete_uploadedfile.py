# Generated by Django 5.1.5 on 2025-03-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_app', '0003_uploadedfile_delete_csvdata_delete_productdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='UploadedFile',
        ),
    ]
