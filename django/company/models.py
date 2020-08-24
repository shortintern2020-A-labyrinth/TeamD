from django.db import models

# Create your models here.

class Video(models.Model):
    name = models.CharField(
        max_length=60,
        null=False,
        blank=False
    )
    description = models.TextField(
        max_length=5000,
        null=False,
        blank=False
    )
    youtube_url = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    company_id = models.IntegerField(
        null=False,
        blank=False
    )

class Company(models.Model):
    name = models.CharField(
            max_length=60,
            null=False,
            blank=False
    )
    email = models.EmailField()
    password = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.SmallIntegerField()
    tokens =  models.TextField()

class Category(models.Model):
    id = models.IntegerField(
        null=False,
        blank=False,
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
