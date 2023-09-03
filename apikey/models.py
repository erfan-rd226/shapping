import jwt

from typing import Iterable, Optional

from django.conf import settings

from django.db import models
from django.contrib.auth.models import User


class ApiKey(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    expire_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    roll = models.CharField(max_length=50)
    token = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


#THIS CODE ABOUT JSON FOR API KEY

# {
#     "user": 1,
#     "expire_time": "2024-01-01",
#     "is_active": true,
#     "roll":"5/1/min"
# }