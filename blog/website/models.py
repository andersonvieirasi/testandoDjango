from django.conf import settings
from django.db import models


class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologias'
    CR = "CR", "Curiosidades"
    GR = 'GR', "Geral"
    
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Título", max_length=100)
    text = models.TextField("Texto")
    categories = models.CharField(
    		"Categoria",
    		max_length = 2,
    		choices=Categorias.choices,
    		default=Categorias.GR,)
    approved = models.BooleanField("Aprovado", default=True)

    created_date = models.DateTimeField("Data da Criação", auto_now_add=True)
    published_date = models.DateTimeField("Data da Publicação", blank=True, 
    	                        null=True, auto_now=True)

    image = models.ImageField("Imagem", upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title


