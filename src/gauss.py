import numpy as np
import matplotlib.pyplot as plt


epsilon_0 = 8.854e-12   


Q = float(input("Enter charge Q (in Coulombs): "))
r_min = float(input("Enter minimum distance r_min (in meters): "))
r_max = float(input("Enter maximum distance r_max (in meters): "))


r = np.linspace(r_min, r_max, 100)


E = Q / (4 * np.pi * epsilon_0 * r**2)


plt.plot(r, E)
plt.xlabel("Distance r (m)")
plt.ylabel("Electric Field E (N/C)")
plt.title("Electric Field vs Distance (Gauss's Law)")
plt.grid(True)


plt.savefig("gauss_law_field.png")
plt.show()

print("Graph saved as gauss_law_field.png")
