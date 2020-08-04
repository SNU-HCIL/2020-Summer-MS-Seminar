import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    start_date = models.DateTimeField('time started', auto_now_add=True, editable=False)
    end_date = models.DateTimeField('time ended', null=True, blank=True)
    result_text = models.CharField(max_length=4, null=True, blank=True)
    game_length = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return "Game Started at " + str(self.start_date.strftime('%Y-%m-%d %H:%M')) + " - " + str(self.result_text)