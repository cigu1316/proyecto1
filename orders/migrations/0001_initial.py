# Generated by Django 4.1.3 on 2022-12-31 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('cash', 'cash'), ('card', 'card')], max_length=4)),
            ],
        ),
    ]