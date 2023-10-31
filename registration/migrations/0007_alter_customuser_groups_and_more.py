# Generated by Django 4.2.5 on 2023-09-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('registration', '0006_rename_farmer_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='this group belongs to', related_name='customer_set', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Permission to user.', related_name='farmers_related', to='auth.permission', verbose_name='user_permissions'),
        ),
    ]