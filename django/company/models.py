from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


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
    category_id = models.IntegerField(
        null=False,
        blank=False
    )


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
