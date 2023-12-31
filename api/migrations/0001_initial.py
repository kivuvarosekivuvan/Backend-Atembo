# Generated by Django 4.2.5 on 2023-09-09 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50)),
                ('name', models.CharField(default='Unknown', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FlowRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('flow_rate', models.FloatField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.device')),
            ],
        ),
    ]
