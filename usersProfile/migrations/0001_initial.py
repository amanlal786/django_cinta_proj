# Generated by Django 2.2.16 on 2021-08-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('skills', models.CharField(max_length=300)),
                ('image1', models.ImageField(height_field=1280, upload_to='profile_pics', width_field=960)),
                ('image2', models.ImageField(height_field=1280, upload_to='profile_pics', width_field=960)),
            ],
        ),
    ]
