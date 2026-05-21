from django.db import models
from django.contrib.auth.models import User

class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    url = models.URLField()
    is_active = models.BooleanField(default=True)
    last_content = models.TextField(blank=True, null=True)
    change_count = models.IntegerField(default=0)