from django.db import models

# Create your models here.

class tttUser(models.Model):
    userId = models.CharField(max_length=200)
    
    win = models.IntegerField()
    lose = models.IntegerField()
    draw = models.IntegerField()
    
    def __str__(self):
        return self.userId;
    