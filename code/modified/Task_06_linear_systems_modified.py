# how many vehicles of each type did a SACCO run today?
# Three unknowns instead of two. From total seats, fuel and crew we work out the
# number of 14-seater matatus, 33-seater minibuses and 51-seater buses.
import numpy as np

# x = 14-seater matatus, y = 33-seater minibuses, z = 51-seater buses
#
#               matatu  minibus  bus
A = np.array([
    [14.0, 33.0, 51.0],   # seats per vehicle
    [30.0, 55.0, 80.0],   # litres of fuel per vehicle per day
    [ 2.0,  2.0,  3.0]    # crew per vehicle
])

# Totals recorded by the SACCO office for the day
b = np.array([542.0, 950.0, 44.0])   # seats, litres, crew

solution = np.linalg.solve(A, b)
residual = b - A @ solution

for name, value in zip(["14-seater matatus", "33-seater minibuses", "51-seater buses"], solution):
    print(f"{name}: {value:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual norm:", np.linalg.norm(residual))
print(f"Determinant of A: {np.linalg.det(A):.1f}")
print(f"Condition number of A: {np.linalg.cond(A):.1f}")
