# Generated by Django 3.0.1 on 2022-03-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityapp', '0002_auto_20220311_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='famous',
            name='pers2',
            field=models.CharField(max_length=30, verbose_name='Pers2'),
        ),
    ]
