import numpy as np
import matplotlib.pyplot as plt


K = 8.988e9


try:
    q1 = float(input("Enter charge q1 (C): "))
    q2 = float(input("Enter charge q2 (C): "))
    r_min = float(input("Enter minimum distance (m): "))
    r_max = float(input("Enter maximum distance (m): "))
    n = int(input("Enter number of points: "))
except:
    print("\nInput not detected. Using default values.\n")
    q1 = 1e-6
    q2 = 2e-6
    r_min = 0.01
    r_max = 0.1
    n = 100


distance = np.linspace(r_min, r_max, n)


force = K * q1 * q2 / (distance ** 2)


r_test = 0.01
F_test = K * q1 * q2 / (r_test ** 2)

print(f"Electrostatic force at r = {r_test} m:")
print(f"F = {F_test:.2f} N")

plt.plot(distance, force)
plt.xlabel("Distance (m)")
plt.ylabel("Force (N)")
plt.title("Coulomb Force vs Distance")
plt.grid(True)

plt.savefig("coulomb_force.png")
plt.show()
