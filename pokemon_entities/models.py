from email.quoprimime import unquote
from operator import mod
from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', null=True)
    
    def __str__(self) -> str:
        return self.title
    
class PokemonEntity(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.pokemon_title} ({self.latitude}, {self.longitude})'