# break-even point of a T-shirt printing business.
# Profit(q) = revenue - costs. The break-even quantity is the root of Profit(q) = 0.
# Solved with a hand-written bisection loop and with fixed-point iteration.
import numpy as np
import matplotlib.pyplot as plt

PRICE = 120.0          # selling price per shirt (KSh)
UNIT_COST = 40.0       # material cost per shirt (KSh)
FIXED_COST = 45_000.0  # rent, machine, licence per month (KSh)
OVERTIME = 300.0       # overtime/maintenance cost grows like 300*sqrt(q)

def profit(q):
    return PRICE*q - (FIXED_COST + UNIT_COST*q + OVERTIME*np.sqrt(q))

# Bisection written out by hand
a, b = 100.0, 2000.0
assert profit(a) * profit(b) < 0, "the bracket must contain a sign change"
bisection_steps = 0
while (b - a) > 1e-8:
    mid = (a + b) / 2
    if profit(a) * profit(mid) <= 0:
        b = mid
    else:
        a = mid
    bisection_steps += 1
q_bisect = (a + b) / 2

# Fixed-point form: q = (FIXED_COST + OVERTIME*sqrt(q)) / (PRICE - UNIT_COST)
def g(q):
    return (FIXED_COST + OVERTIME*np.sqrt(q)) / (PRICE - UNIT_COST)

q = 500.0
history = [q]
for _ in range(100):
    q_new = g(q)
    history.append(q_new)
    if abs(q_new - q) < 1e-8:
        break
    q = q_new

print(f"Bisection break-even quantity: {q_bisect:.4f} shirts in {bisection_steps} steps")
print(f"Fixed-point break-even quantity: {history[-1]:.4f} shirts in {len(history)-1} iterations")
print(f"Profit at the root: KSh {profit(q_bisect):.6f}")
print(f"Shirts to sell to make a profit: {int(np.ceil(q_bisect))}")
print(f"Profit at 600 shirts: KSh {profit(600):,.2f}")
print(f"Profit at 800 shirts: KSh {profit(800):,.2f}")

qs = np.linspace(100, 1200, 300)
plt.plot(qs, profit(qs), label="Profit(q)")
plt.axhline(0, linewidth=0.8, color="black")
plt.axvline(q_bisect, linestyle="--", color="red", label=f"Break-even = {q_bisect:.0f} shirts")
plt.xlabel("Shirts sold per month")
plt.ylabel("Profit (KSh)")
plt.title("Break-even point of the T-shirt business")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_10_modified.png", dpi=150, bbox_inches="tight")
plt.show()
