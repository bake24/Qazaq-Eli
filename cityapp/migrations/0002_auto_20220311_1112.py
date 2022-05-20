# Generated by Django 3.0.1 on 2022-03-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Famous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30, verbose_name='City name')),
                ('pers1', models.CharField(max_length=30, verbose_name='Pers1')),
                ('pers2', models.CharField(max_length=15, verbose_name='Pers2')),
                ('pers3', models.CharField(max_length=100, verbose_name='Pers3')),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='place3',
            field=models.CharField(max_length=100, verbose_name='Place3'),
        ),
    ]