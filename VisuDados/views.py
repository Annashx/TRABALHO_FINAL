from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    dt = [] 
    la = []
    k = []
    val = Data.objects.all()
    for v in val:
        dt.append(v.dado)
        k.append(v.dado2)
        la.append(int(v.label))
    return render(request, 'index.html', {'dt2': dt, 'la2': la, 'k2': k})