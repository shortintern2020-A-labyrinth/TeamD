# Generated by Django 3.1 on 2020-08-26 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20200825_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('type', models.IntegerField()),
                ('company_id', models.IntegerField()),
            ],
        ),
    ]
