from django.db import models


class Author(models.Model):
    user_name = models.CharField(max_length=255, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)


class Blog(models.Model):
    STATUS_DRAFT = 'D'
    STATUS_POSTED = 'P'
    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Drafted'),
        (STATUS_POSTED, 'Posted'),
    ]
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
