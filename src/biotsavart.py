import numpy as np
import matplotlib.pyplot as plt


mu_0 = 4 * np.pi * 1e-7   
I = 5.0                  


r = np.linspace(0.01, 0.1, 100)

B = (mu_0 * I) / (2 * np.pi * r)


plt.plot(r, B)
plt.xlabel("Distance (m)")
plt.ylabel("Magnetic Field (T)")
plt.title("Magnetic Field vs Distance (Biot-Savart Law)")
plt.grid(True)

plt.savefig("biot_savart_field.png", dpi=300)
plt.show()
