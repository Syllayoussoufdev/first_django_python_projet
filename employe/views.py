from django.shortcuts import render
from .models import Employe
 
# Create your views here. create a view for the employee app

def list_emloyes(request):
    employes = Employe.objects.all()