from django.db import models


class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    memo =  models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
