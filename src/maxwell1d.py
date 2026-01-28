import numpy as np
import matplotlib.pyplot as plt


epsilon_0 = 8.854e-12    
rho = 1e-6               


x = np.linspace(-1, 1, 200)


E = (rho / epsilon_0) * x


plt.plot(x, E)
plt.xlabel("x (m)")
plt.ylabel("Electric Field (N/C)")
plt.title("Electric Field vs Position (Maxwell's Equation - 1D)")
plt.grid(True)
plt.savefig("maxwell_1d_field.png", dpi=300)
plt.show()
