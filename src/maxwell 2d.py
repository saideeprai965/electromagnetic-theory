import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 20)
y = np.linspace(-1, 1, 20)
X, Y = np.meshgrid(x, y)


k = 5
Ex = k * X
Ey = np.zeros_like(Y)

plt.figure(figsize=(6, 6))
plt.quiver(X, Y, Ex, Ey)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Electric Field Vector Plot (Linear Field)")
plt.grid(True)
plt.axis("equal")

plt.show()
