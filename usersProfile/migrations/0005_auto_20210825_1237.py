# Generated by Django 2.0 on 2021-08-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersProfile', '0004_auto_20210825_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='save_age',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
        migrations.AddField(
            model_name='user',
            name='save_image1',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
        migrations.AddField(
            model_name='user',
            name='save_image2',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
        migrations.AddField(
            model_name='user',
            name='save_name',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
        migrations.AddField(
            model_name='user',
            name='save_skills',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
    ]
