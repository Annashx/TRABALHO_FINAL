from django.shortcuts import render
from .models import *
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# Create your views here.


def index(request):
    dt = [] 
    la = []
    k = []
    val = Data.objects.all()
    for v in val:
        dt.append(v.dado)
        k.append(v.dado2)
        la.append(v.label)
    return render(request, 'index.html', {'dt2': dt, 'la2': la, 'k2': k})

def achak(c, t):
    reg = LinearRegression().fit(c.reshape(-1, 1), t)
    return reg.coef_

kcerto = 0.52