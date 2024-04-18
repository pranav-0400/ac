# Generated by Django 5.0.2 on 2024-02-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('category', models.CharField(choices=[('C', 'Computer'), ('M', 'Mobile'), ('T', 'Tablet')], max_length=5)),
                ('label', models.CharField(choices=[('N', 'New'), ('R', 'Refurbished'), ('U', 'Used')], max_length=5)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
