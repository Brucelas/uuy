# Generated by Django 4.1.3 on 2023-06-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('newPage', '0004_usuario_is_active_usuario_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(related_name='usuarios', to='auth.group'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(related_name='usuarios', to='auth.permission'),
        ),
    ]