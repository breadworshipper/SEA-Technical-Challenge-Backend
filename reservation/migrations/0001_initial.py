# Generated by Django 4.0.10 on 2024-06-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('type_of_service', models.CharField(choices=[('Haircuts and styling', 'haircuts and styling'), ('Manicure and pedicure', 'manicure and pedicure'), ('Facial treatment', 'facial treatment')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]