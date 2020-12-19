#!/usr/bin/env python3

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

rel_tol = 3e-12         # Relative Tolerance
abs_tol = 1e-12         # Absolute tolerance


def F(X, t, params):

    dX = np.ones(shape=X.shape)

    # Cinemática:
    vx = X[2]
    vy = X[3]

    dX[0] = vx
    dX[1] = vy
    
    # Dinámica:
    viento = -5 # en contra
    g = -10

    # Acá hay un cambio de fase:
    empuje = (vx - viento) * (viento < vx) * 100 * (viento + 7.024321536125 > vx)

    ax = viento
    ay = g + empuje

    dX[2] = ax
    dX[3] = ay

    return dX


# Posiciones y velocidades iniciales
X0 = np.array([0, 0, 3, 5])

time = np.linspace(0, 0.5, 1000)

Xs = odeint(F, X0, time, args = (None,), rtol = rel_tol, atol = abs_tol)

plt.plot(Xs[:, 0], Xs[:, 1], '.-')

plt.grid(True)
# plt.legend()
plt.xlabel('Suelo')
plt.ylabel('Aire')
plt.show()
