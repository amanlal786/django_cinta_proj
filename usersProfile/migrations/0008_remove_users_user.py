# Generated by Django 2.0 on 2021-08-25 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersProfile', '0007_users_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user',
        ),
    ]
