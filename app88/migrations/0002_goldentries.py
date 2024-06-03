# Generated by Django 5.0.2 on 2024-03-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app88', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goldentries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('trade_description', models.CharField(max_length=200)),
                ('trade_image', models.ImageField(upload_to='tradeimages')),
            ],
        ),
    ]