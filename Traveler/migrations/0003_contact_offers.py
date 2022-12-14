# Generated by Django 4.1.3 on 2022-11-10 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Traveler', '0002_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.IntegerField()),
                ('offer', models.IntegerField()),
            ],
        ),
    ]
