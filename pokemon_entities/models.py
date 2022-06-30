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
    
    def __str__(self) -> str:
        return f'Latitude: {self.latitude}, Longitude: {self.longitude}'