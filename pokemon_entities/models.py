from email.quoprimime import unquote
from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', null=True)
    
    def __str__(self) -> str:
        return self.title