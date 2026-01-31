import numpy as np
import matplotlib.pyplot as plt


epsilon0 = 8.854e-12
Q = 1e-6

x = np.linspace(-1, 1, 20)
y = np.linspace(-1, 1, 20)
X, Y = np.meshgrid(x, y)


r = np.sqrt(X*2 + Y*2) + 1e-9


Ex = Q * X / (4 * np.pi * epsilon0 * r**3)
Ey = Q * Y / (4 * np.pi * epsilon0 * r**3)

plt.figure(figsize=(6, 6))
plt.quiver(X, Y, Ex, Ey)
plt.plot(x, x, 'k')     
plt.plot(x, -x, 'k')    
plt.xlabel("x")
plt.ylabel("y")
plt.title("Electric Field Vector Plot (2D)")
plt.grid(True)
plt.axis("equal")

plt.show()
