# Generated by Django 5.1.2 on 2024-10-17 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('num_serie', models.CharField(max_length=20, unique=True)),
                ('categoria', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]