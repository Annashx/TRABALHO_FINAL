from django.shortcuts import render
from .models import *
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# Create your views here.


def index(request):
    temp = [] 
    conc = []
    ns = []
    val = Data.objects.all()
    for v in val:
        temp.append(v.temperatura)
        conc.append(v.concentracao)
        ns.append(v.temperatura * v.concentracao)
    return render(request, 'index.html', {'temp2': temp, 'conc2': conc, 'ns2': ns})

def achak(c, t):
    reg = LinearRegression().fit(c.reshape(-1, 1), t)
    return reg.coef_

kcerto = 0.52