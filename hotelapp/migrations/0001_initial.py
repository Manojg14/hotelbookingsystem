# Generated by Django 5.2 on 2025-06-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField(max_length=10)),
                ('phonenumber', models.IntegerField(max_length=10)),
                ('emailid', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('adults', models.IntegerField()),
                ('kids', models.IntegerField()),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('card', 'Card')], max_length=10)),
                ('specialrequest', models.CharField(max_length=100)),
            ],
        ),
    ]
