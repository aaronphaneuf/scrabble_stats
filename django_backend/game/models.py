from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Token(models.Model):
    class Meta:
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS

class User(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    #player3 = models.ForeignKey("Word" , default="", on_delete=models.CASCADE)
    #user = models.ManyToManyField("Word", default=1, related_name="player1")
    letters = models.ManyToManyField("Word")

    
    #user = models.ManyToManyField("Word")


    def __str__(self):
        return self.name

class Game(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    #player_info = models.ManyToManyField("Word", default=1, related_name="player_info")
    player = models.ManyToManyField("User")
    winner = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)


class Word(models.Model):
    game = models.ForeignKey(Game, related_name='word', on_delete=models.CASCADE)
    turn = models.IntegerField()
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='letter') # related_name='words',)
    word = models.CharField(max_length=255)
    score = models.IntegerField()
    

    def __str__(self):
        return str(self.player.name)

   


