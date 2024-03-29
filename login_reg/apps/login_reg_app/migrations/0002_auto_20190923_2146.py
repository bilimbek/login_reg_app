# Generated by Django 2.2.5 on 2019-09-23 21:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Confirm_password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='First_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Password',
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='bil@icloud.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='pw_hash',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='user', max_length=255),
            preserve_default=False,
        ),
    ]
