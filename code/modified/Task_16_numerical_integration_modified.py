# distance covered by a matatu from speedometer readings.
# Speed is logged every 10 seconds between two stages. Distance is the integral of
# speed over time (area under the speed-time graph).
import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt

time_s = np.arange(0, 130, 10, dtype=float)           # 0, 10, ..., 120 s
speed_kmh = np.array([0, 18, 35, 48, 56, 60, 62, 60, 55, 45, 30, 12, 0], dtype=float)
speed_ms = speed_kmh / 3.6                            # km/h -> m/s

distance_trapezoid = np.trapezoid(speed_ms, time_s)
distance_simpson = simpson(speed_ms, x=time_s)

print(f"Distance, trapezoidal rule:    {distance_trapezoid:.1f} m")
print(f"Distance, Simpson's rule:      {distance_simpson:.1f} m")
print(f"Trapezoid vs Simpson difference: {abs(distance_simpson - distance_trapezoid):.1f} m")
print(f"Average speed: {distance_simpson/time_s[-1]*3.6:.1f} km/h")

# Using only every second reading (20 s spacing) shows the effect of fewer samples
print(f"Trapezoid with readings every 20 s: {np.trapezoid(speed_ms[::2], time_s[::2]):.1f} m")
print(f"Simpson with readings every 20 s:   {simpson(speed_ms[::2], x=time_s[::2]):.1f} m")

plt.plot(time_s, speed_ms, marker="o")
plt.fill_between(time_s, speed_ms, alpha=0.3, label=f"Area = distance = {distance_simpson:.0f} m")
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Matatu speed between two stages")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_16_modified.png", dpi=150, bbox_inches="tight")
plt.show()
