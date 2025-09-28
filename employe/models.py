from django.db import models

# Create your models here.
class Employe(models.Model):
    employe_nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    poste = models.CharField(max_length=100)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.employe_nom} - {self.poste}"
