# Generated by Django 4.2.7 on 2023-11-30 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='importfile',
            name='file_image',
            field=models.ImageField(default='images/questionmark.jpeg', upload_to='images/'),
        ),
    ]