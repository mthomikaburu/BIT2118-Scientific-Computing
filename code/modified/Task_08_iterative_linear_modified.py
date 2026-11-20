# daily output needed from 4 linked business units.
# Each unit uses part of the other units' output (a Leontief input-output model).
# x = C x + d  becomes  (I - C) x = d, solved by Jacobi and Gauss-Seidel.
import numpy as np
import matplotlib.pyplot as plt

units = ["Farm", "Mill", "Bakery", "Transport"]

# C[i, j] = units of i's output needed to make 1 unit of j's output
C = np.array([
    [0.10, 0.30, 0.05, 0.05],
    [0.05, 0.10, 0.35, 0.05],
    [0.02, 0.03, 0.05, 0.10],
    [0.10, 0.10, 0.10, 0.05]
])
d = np.array([50.0, 30.0, 120.0, 40.0])   # outside customer demand (KSh '000)

A = np.eye(4) - C
b = d

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        errors.append(np.linalg.norm(x_new - x, ord=np.inf))
        x = x_new
        if errors[-1] < tol:
            break
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        errors.append(np.linalg.norm(x - old, ord=np.inf))
        if errors[-1] < tol:
            break
    return x, errors

x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

diag = np.abs(np.diag(A))
off = np.abs(A).sum(axis=1) - diag
print("Strictly diagonally dominant:", bool(np.all(diag > off)))
for u, xj, xg, xe, dem in zip(units, x_j, x_gs, x_exact, d):
    print(f"{u:<10} outside demand={dem:6.1f}  required output: Jacobi={xj:8.3f}  Gauss-Seidel={xg:8.3f}  direct={xe:8.3f}")
print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))

plt.semilogy(err_j, marker=".", label="Jacobi")
plt.semilogy(err_gs, marker=".", label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence for the input-output model")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_08_modified.png", dpi=150, bbox_inches="tight")
plt.show()
