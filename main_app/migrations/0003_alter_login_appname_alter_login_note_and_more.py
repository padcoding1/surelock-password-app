# Generated by Django 5.0.7 on 2024-08-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_password_appname_password_note_password_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='appname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='note',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]