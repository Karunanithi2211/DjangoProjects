# Generated by Django 4.1.3 on 2023-01-06 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registerform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'datas',
            },
        ),
    ]
