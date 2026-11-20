# cheapest chicken-feed mix for a poultry farmer.
# Mix maize and soya meal to make 100 kg of feed at minimum cost while meeting a
# minimum protein level and a minimum energy level (two constraints + a total).
import numpy as np
from scipy.optimize import minimize, linprog

# Per kg:            maize   soya
COST = np.array([     45.0,   95.0])    # KSh
PROTEIN = np.array([  0.09,   0.44])    # kg protein per kg
ENERGY = np.array([   3350,   2450])    # kcal per kg

BATCH = 100.0                 # kg of feed to make
MIN_PROTEIN = 0.18 * BATCH    # at least 18% protein
MIN_ENERGY = 2900 * BATCH     # at least 2900 kcal/kg on average

def cost(z):
    return COST @ z

constraints = [
    {"type": "eq",   "fun": lambda z: z.sum() - BATCH},
    {"type": "ineq", "fun": lambda z: PROTEIN @ z - MIN_PROTEIN},
    {"type": "ineq", "fun": lambda z: (ENERGY @ z - MIN_ENERGY) / 1000},
]

solution = minimize(cost, x0=[50.0, 50.0], method="SLSQP",
                    bounds=[(0, None), (0, None)], constraints=constraints)
maize, soya = solution.x

print("Optimization success:", solution.success)
print(f"Maize: {maize:.2f} kg   Soya meal: {soya:.2f} kg")
print(f"Protein: {PROTEIN @ solution.x / BATCH:.2%}   Energy: {ENERGY @ solution.x / BATCH:.0f} kcal/kg")
print(f"Minimum cost: KSh {solution.fun:,.2f} per 100 kg  (KSh {solution.fun/BATCH:.2f} per kg)")

# Cross-check with a linear-programming solver (the problem is linear)
lp = linprog(COST, A_ub=[-PROTEIN, -ENERGY], b_ub=[-MIN_PROTEIN, -MIN_ENERGY],
             A_eq=[[1, 1]], b_eq=[BATCH], bounds=[(0, None), (0, None)])
print(f"linprog check: maize = {lp.x[0]:.2f} kg, soya = {lp.x[1]:.2f} kg, cost = KSh {lp.fun:,.2f}")

# Comparison with a simple 50/50 mix
half = np.array([50.0, 50.0])
print(f"50/50 mix: protein {PROTEIN @ half / BATCH:.1%}, cost KSh {COST @ half:,.2f} "
      f"-> optimum saves KSh {COST @ half - solution.fun:,.2f}")
