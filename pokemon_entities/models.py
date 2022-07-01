from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', null=True)
    
    def __str__(self) -> str:
        return self.title
    
class PokemonEntity(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entities')
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    strength = models.IntegerField(default=1)
    defence = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.pokemon.title} ({self.latitude}, {self.longitude})'