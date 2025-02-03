from django.db import models
from django.contrib.auth.models import User

class CodeSnippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    analysis = models.TextField(blank=True, null=True)
    