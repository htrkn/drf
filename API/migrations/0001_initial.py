# Generated by Django 2.2.10 on 2020-02-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kurlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doviz_ismi', models.CharField(max_length=10)),
                ('alis', models.FloatField()),
                ('satis', models.FloatField()),
                ('fark', models.FloatField()),
                ('kur_kodu', models.CharField(max_length=10)),
            ],
        ),
    ]
