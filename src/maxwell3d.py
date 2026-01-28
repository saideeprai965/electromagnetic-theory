import numpy as np
import matplotlib.pyplot as plt

eps0 = 8.854e-12
charge = 1e-6
points = np.linspace(-1, 1, 8)
X, Y, Z = np.meshgrid(points, points, points)

distance = np.sqrt(X*2 + Y2 + Z*2) + 1e-9

E_mag = charge / (4 * np.pi * eps0 * distance**2)


figure = plt.figure(figsize=(7, 6))
axis = figure.add_subplot(111, projection='3d')

scatter = axis.scatter(
    X, Y, Z,
    c=E_mag,
    cmap='viridis'
)

axis.set_xlabel("x")
axis.set_ylabel("y")
axis.set_zlabel("z")
axis.set_title("Maxwell's Equation (3D)")

plt.show()
