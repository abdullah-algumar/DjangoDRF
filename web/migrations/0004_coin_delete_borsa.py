# Generated by Django 4.2.4 on 2023-08-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_borsa_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=5)),
                ('buying', models.IntegerField()),
                ('buying_str', models.CharField(max_length=50)),
                ('selling', models.IntegerField()),
                ('selling_str', models.CharField(max_length=50)),
                ('rate', models.IntegerField()),
                ('time', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('datetime', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Coin',
                'verbose_name_plural': 'Coins',
                'db_table': 'coins',
            },
        ),
        migrations.DeleteModel(
            name='Borsa',
        ),
    ]
