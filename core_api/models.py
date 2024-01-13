from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        choices={"active": "Active", "deleted": "Deleted"},
        default="active",
        max_length=25,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    status = models.CharField(
        choices={"active": "Active", "deleted": "Deleted"},
        default="active",
        max_length=25,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    source_comment = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    status = models.CharField(
        choices={"active": "Active", "deleted": "Deleted"},
        default="active",
        max_length=25,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Vote(models.Model):
    post = models.ForeignKey(Post, related_name="votes", on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "voted_by")
