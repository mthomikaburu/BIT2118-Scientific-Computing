# flu spreading through a campus of 1,000 students (SIR).
# Three linked ODEs instead of one:
# dS/dt = -beta*S*I/N,  dI/dt = beta*S*I/N - gamma*I,  dR/dt = gamma*I
# solve_ivp handles the whole system at once.
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

N = 1000.0          # students
beta = 0.40         # infection rate per day
gamma = 0.10        # recovery rate per day (about 10 days sick)
y0 = [N - 5, 5.0, 0.0]   # S, I, R at day 0

def sir(t, y):
    S, I, R = y
    new_infections = beta * S * I / N
    recoveries = gamma * I
    return [-new_infections, new_infections - recoveries, recoveries]

t_eval = np.linspace(0, 120, 601)
solution = solve_ivp(sir, (0, 120), y0, t_eval=t_eval, rtol=1e-8, atol=1e-8)
S, I, R = solution.y

peak = np.argmax(I)
print("Solver success:", solution.success)
print(f"Basic reproduction number R0 = beta/gamma = {beta/gamma:.1f}")
print(f"Peak: {I[peak]:.0f} students sick at the same time, on day {solution.t[peak]:.1f}")
print(f"Total ever infected by day 120: {R[-1] + I[-1]:.0f} of {N:.0f}")
print(f"Never infected: {S[-1]:.0f}")
print(f"Conservation check, max |S+I+R-N| = {np.max(np.abs(S + I + R - N)):.2e}")

plt.plot(solution.t, S, label="Susceptible")
plt.plot(solution.t, I, label="Infected")
plt.plot(solution.t, R, label="Recovered")
plt.xlabel("Time (days)")
plt.ylabel("Number of students")
plt.title("SIR model of flu on a campus")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_18_modified.png", dpi=150, bbox_inches="tight")
plt.show()
