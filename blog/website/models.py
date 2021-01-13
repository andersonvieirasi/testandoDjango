from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Título", max_length=100)
    text = models.TextField("Texto")
    created_date = models.DateTimeField("Data da Criação", auto_now_add=True)
    published_date = models.DateTimeField("Data da Publicação", blank=True, 
    	                        null=True, auto_now=True)

    def __str__(self):
        return self.title