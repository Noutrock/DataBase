from django.db import models

# Create your models here.

class ModelLogin(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"Usuario: {self.id} {self.user} {self.password}"

