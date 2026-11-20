# growth of a mobile app's active users.
# The original fitted a quadratic. Growth data is better described by an
# exponential model  y = a * exp(b * month). We fit it and forecast month 12.
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

month = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
active_users = np.array([520, 610, 760, 905, 1120, 1340, 1650, 1990], dtype=float)

def exponential(x, a, b):
    return a * np.exp(b * x)

def straight_line(x, m, c):
    return m * x + c

(a, b), covariance = curve_fit(exponential, month, active_users, p0=[500, 0.2])
(m, c), _ = curve_fit(straight_line, month, active_users)

def rmse(model, *params):
    return np.sqrt(np.mean((active_users - model(month, *params))**2))

a_err, b_err = np.sqrt(np.diag(covariance))
print(f"Exponential model: users = {a:.1f} * exp({b:.4f} * month)")
print(f"Parameter uncertainty: a +/- {a_err:.1f}, b +/- {b_err:.4f}")
print(f"Monthly growth rate: {np.exp(b) - 1:.1%}")
print(f"Doubling time: {np.log(2)/b:.2f} months")
print(f"RMSE exponential: {rmse(exponential, a, b):.1f} users")
print(f"RMSE straight line: {rmse(straight_line, m, c):.1f} users")
print(f"Forecast for month 12: exponential = {exponential(12, a, b):.0f}, straight line = {straight_line(12, m, c):.0f}")

x_plot = np.linspace(1, 12, 200)
plt.scatter(month, active_users, label="Measured", zorder=3)
plt.plot(x_plot, exponential(x_plot, a, b), label="Exponential fit")
plt.plot(x_plot, straight_line(x_plot, m, c), linestyle="--", label="Straight-line fit")
plt.xlabel("Month")
plt.ylabel("Active users")
plt.title("App user growth: fitted models and forecast")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_14_modified.png", dpi=150, bbox_inches="tight")
plt.show()
