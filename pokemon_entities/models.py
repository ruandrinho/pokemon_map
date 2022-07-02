from tkinter import CASCADE
from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Название по-английски')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Название по-японски')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images', null=True, verbose_name='Изображение')
    evolved_from = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='evolved_to', verbose_name='Из кого эволюционировал')
    
    def __str__(self) -> str:
        return self.title
    
class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entities', verbose_name='Вид покемона')
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Когда появляется')
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Когда исчезает')
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Атака')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')

    def __str__(self) -> str:
        return f'{self.pokemon.title} ({self.latitude}, {self.longitude})'