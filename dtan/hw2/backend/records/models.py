from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Record(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    win = models.IntegerField('win')
    draw = models.IntegerField('draw')
    lose = models.IntegerField('lose')

    def as_dict(self):
        return {
            'total': self.win + self.draw + self.lose,
            'win': self.win,
            'draw': self.draw,
            'lose': self.lose
        }

    def __str__(self):
        return 'w: ' + self.win + ', d: ' + self.draw + ', l: ' + self.lose