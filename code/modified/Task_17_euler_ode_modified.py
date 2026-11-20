# tilapia growing in a fish pond (logistic growth).
# dP/dt = r * P * (1 - P/K). Unlike cooling, growth is slow at first, fast in the
# middle and levels off at the pond's carrying capacity K. Solved with Euler for
# two step sizes and compared with the exact solution.
import numpy as np
import matplotlib.pyplot as plt

r = 0.35      # growth rate per month
K = 2000.0    # carrying capacity of the pond (fish)
P0 = 100.0    # fish stocked at month 0
END = 24.0    # months

def growth_rate(P):
    return r * P * (1 - P / K)

def euler(h):
    t = np.arange(0, END + h, h)
    P = np.zeros_like(t)
    P[0] = P0
    for i in range(len(t) - 1):
        P[i + 1] = P[i] + h * growth_rate(P[i])
    return t, P

def exact(t):
    return K / (1 + (K - P0) / P0 * np.exp(-r * t))

for h in (2.0, 0.5):
    t, P = euler(h)
    print(f"h = {h} months: fish at month 12 = {P[t == 12][0]:.1f}, at month 24 = {P[-1]:.1f}, "
          f"largest error = {np.max(np.abs(P - exact(t))):.1f} fish")
    plt.plot(t, P, marker="o", markersize=3, label=f"Euler, h = {h}")

print(f"Exact: fish at month 12 = {exact(12):.1f}, at month 24 = {exact(24):.1f}")
t_half = np.log((K - P0) / P0) / r
print(f"Population reaches K/2 = {K/2:.0f} (fastest growth) at month {t_half:.2f}")

t_fine = np.linspace(0, END, 300)
plt.plot(t_fine, exact(t_fine), color="black", label="Exact solution")
plt.axhline(K, linestyle=":", color="grey", label="Carrying capacity K")
plt.xlabel("Time (months)")
plt.ylabel("Number of fish")
plt.title("Logistic growth of tilapia in a pond")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_17_modified.png", dpi=150, bbox_inches="tight")
plt.show()
