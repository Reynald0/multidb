from django.db import models

class MiApp2Model(models.Model):
    nombre = models.CharField(max_length=20)