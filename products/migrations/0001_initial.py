# Generated by Django 4.1.7 on 2023-02-16 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('description', models.CharField(max_length=254)),
                ('unique_id', models.CharField(max_length=254, unique=True)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=254, upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productmain')),
            ],
        ),
    ]
