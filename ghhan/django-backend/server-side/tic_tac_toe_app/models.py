import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='games', on_delete=models.CASCADE)
    start_date = models.DateTimeField('time started')
    end_date = models.DateTimeField('time ended', auto_now_add=True, editable=False)
    result_text = models.CharField(max_length=4, null=True, blank=True)
    game_turns = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return "Game by"+ str(self.player) + " Started at " + str(self.start_date.strftime('%Y-%m-%d %H:%M')) + " - " + str(self.result_text)