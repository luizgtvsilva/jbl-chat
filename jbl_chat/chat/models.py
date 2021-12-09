from django.db import models
from django.db.models.base import Model

class User(models.Model):

    class Meta:

        db_table = 'user'

    user_firstname = models.CharField(max_length=200)
    user_lastname = models.CharField(max_length=200)

class Chat(models.Model):

    class Meta:

        db_table = 'chat'
    
    from_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    message = models.CharField(max_length=1000)
    to_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')