from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


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
    tokens = models.TextField()


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
    company_id = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    category_id = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )


class Url(models.Model):
    value = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    typex = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    company_id = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )


class Keyword(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    video_id = models.ForeignKey(
        Video,
        on_delete=models.CASCADE
    )


class Location(models.Model):
    name = models.CharField(
        max_length=255,
    )
    video_id = models.ForeignKey(
        Video,
        on_delete=models.CASCADE
    )
