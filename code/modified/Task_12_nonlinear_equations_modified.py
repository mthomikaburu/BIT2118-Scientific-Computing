# locating a phone from two cell towers, plus a polynomial.
# Part 1 (nonlinear system): each tower knows its distance to the phone, giving two
# circles. Their intersections are the possible phone positions.
# Part 2 (polynomial): when does a ball thrown from a 20 m roof hit the ground?
import numpy as np
from scipy.optimize import root

# ---- Part 1: two circles (units: km) ----
TOWER_1, R1 = (0.0, 0.0), 5.0
TOWER_2, R2 = (6.0, 0.0), 4.0

def equations(z):
    x, y = z
    return [
        (x - TOWER_1[0])**2 + (y - TOWER_1[1])**2 - R1**2,
        (x - TOWER_2[0])**2 + (y - TOWER_2[1])**2 - R2**2
    ]

for guess in ([3.0, 3.0], [3.0, -3.0]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Phone position (km):", np.round(solution.x, 6))
    print("Residuals:", np.round(equations(solution.x), 12))
    print("Converged:", solution.success)
    print()

# Third tower removes the ambiguity: it measures 3.7 km from (4, 7)
TOWER_3, R3 = np.array([4.0, 7.0]), 3.7
for guess in ([3.0, 3.0], [3.0, -3.0]):
    p = root(equations, guess).x
    print(f"Candidate {np.round(p, 3)} is {np.linalg.norm(p - TOWER_3):.2f} km from tower 3 (measured {R3} km)")
print()

# ---- Part 2: polynomial  h(t) = -4.905 t^2 + 15 t + 20 = 0 ----
coefficients = [-4.905, 15.0, 20.0]
roots = np.roots(coefficients)
print("Roots of -4.905t^2 + 15t + 20:", np.round(roots, 4))
landing = max(roots.real)
print(f"Ball hits the ground after {landing:.3f} s (the negative root is not physical)")
print(f"Check h(t) at landing: {np.polyval(coefficients, landing):.2e} m")
