from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipies(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    steps = models.TextField()
    date_posted = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default="example@email.com")
    telephone = models.CharField(max_length=12, default="44700000000")
    message = models.TextField(default="Type your message here")
    def __str__(self):
        return self.name
