from django.contrib import admin

# Register your models here. enrgistrement de la table \ modeles employe dans l'admin
from .models import *
admin.site.register(Employe)