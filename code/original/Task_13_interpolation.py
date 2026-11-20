import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Hourly temperature measurements
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])

linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

# Estimate every 10 minutes = 1/6 hour
ten_minute_times = np.linspace(8, 14, 37)

linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)

target_time = 10.5  # 10:30
print(f"Linear estimate at {target_time}: {float(linear(target_time)):.2f} C")
print(f"Cubic estimate at {target_time}: {float(cubic(target_time)):.2f} C")

plt.scatter(hours, temperature, label="Hourly measurements")
plt.plot(ten_minute_times, linear_estimates, label="Linear")
plt.plot(ten_minute_times, cubic_estimates, label="Cubic spline")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_13_original.png", dpi=150, bbox_inches="tight")
plt.show()
