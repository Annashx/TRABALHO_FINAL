from django.shortcuts import render
from .models import *
import numpy as np
import matplotlib.pyplot as plt
# Create your views here.
def estimate_coef(x, y):
	# number of observations/points
	n = np.size(x)

	# mean of x and y vector
	m_x = np.mean(x)
	m_y = np.mean(y)

	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x

	# calculating regression coefficients
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return (b_0, b_1)

def index(request):
    temp = [] 
    conc = []
    reg = []
    val = Data.objects.all()
    coef = estimate_coef(np.array(conc), np.array(temp))
    print(coef)
    for v in val:
        temp.append(v.temperatura)
        conc.append(v.concentracao)
        reg.append(0.52 * v.concentracao)
        #reg.append(coef[0] * v.concentracao + coef[1])
    return render(request, 'index.html', {'temp2': temp, 'conc2': conc, 'reg2': reg})

