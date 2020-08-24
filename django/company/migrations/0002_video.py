# Generated by Django 3.1 on 2020-08-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=5000)),
                ('youtube_url', models.CharField(max_length=255)),
                ('company_id', models.IntegerField()),
                ('category_id', models.IntegerField())
            ],
        ),
    ]
