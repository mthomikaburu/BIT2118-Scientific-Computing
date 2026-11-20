# loop currents in a 3-loop DC circuit.
# The resistors (matrix A) never change, but the supply voltages (vector b) change
# with each test. We factor A once with LU and reuse it. We also write out Gaussian
# elimination by hand to show it gives the same answer.
import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

# Mesh (loop) equations  R @ I = V   (ohms, amps, volts)
R = np.array([
    [15.0, -5.0,   0.0],
    [-5.0, 20.0, -10.0],
    [ 0.0, -10.0, 25.0]
])

voltage_scenarios = {
    "Test 1: 12 V on loop 1":           np.array([12.0, 0.0, 0.0]),
    "Test 2: 12 V loop 1, 5 V loop 3":  np.array([12.0, 0.0, 5.0]),
    "Test 3: 24 V on loop 1":           np.array([24.0, 0.0, 0.0]),
    "Test 4: 9 V on loop 2":            np.array([0.0, 9.0, 0.0]),
}

def gaussian_elimination(A, b):
    """Forward elimination with partial pivoting, then back-substitution."""
    A, b = A.astype(float).copy(), b.astype(float).copy()
    n = len(b)
    for k in range(n - 1):
        p = k + np.argmax(np.abs(A[k:, k]))          # pivot row
        A[[k, p]], b[[k, p]] = A[[p, k]], b[[p, k]]
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i, i]
    return x

np.set_printoptions(precision=4, suppress=True)
P, L, U = lu(R)
print("L =\n", L)
print("U =\n", U)
print("P @ L @ U rebuilds R:", np.allclose(P @ L @ U, R))
print()

factors = lu_factor(R)      # factor ONCE
for label, V in voltage_scenarios.items():
    I = lu_solve(factors, V)
    print(label)
    print("  Loop currents (A):", I, "  residual norm:", f"{np.linalg.norm(V - R @ I):.1e}")

first = voltage_scenarios["Test 1: 12 V on loop 1"]
print()
print("Hand-written Gaussian elimination, Test 1:", gaussian_elimination(R, first))
