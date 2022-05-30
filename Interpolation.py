"""
Bartosz Marszalek
Lagrange and Hermite interpolation
Python 3.9
"""
import matplotlib.pyplot as plt
import numpy as np
print("With interpolation would you like to use?")
print("L - Lagrange interpolation\nH - Hermite interpolation")
choice = input()
# Lagrange interpolation
print("Enter interpolating points")
n = int(input("How many points?"))
X = []
Y = []
for i in range(0,n):
    print("x"+str(i+1)+" = ", end='')
    X.append(float(input()))
    print("y"+str(i+1)+" = ", end='')
    Y.append(float(input()))
print("What interval would you like to interpolate? [a,b]")
a = float(input("a = "))
b = float(input("b = "))

#discretisation
h = 100
D = np.linspace(a,b,h)

L = np.ones((n,h))
P = np.zeros(h) #interpolated polinomial
for j in range(0,n):
    for i in range(0,n):
        if i != j:
            L[j] = L[j] * (D - X[i])/(X[j]-X[i])
    P += L[j] * Y[j]

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_title("Lagrange interpolation")
p_max = np.max(P)
p_min = np.min(P)
ax.set_xlim(a, b)
ax.set_ylim(p_min, p_max)
Pol, = ax.plot(0, 0)
Pol.set_xdata(D)
Pol.set_ydata(P)
ax.scatter(X, Y)
plt.show()
