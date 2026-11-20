# hourly electricity use of a cyber cafe.
# Instead of temperatures, the array holds 24 hourly energy readings (kWh) from a
# smart meter. We get total/mean/peak use and convert every reading to a cost in KSh.
import numpy as np
import matplotlib.pyplot as plt

# 24 hourly energy readings in kWh (00:00 to 23:00)
energy_kwh = np.array([
    0.4, 0.4, 0.3, 0.3, 0.3, 0.5,
    0.9, 1.6, 2.8, 3.4, 3.6, 3.8,
    3.9, 3.7, 3.5, 3.6, 3.8, 4.1,
    3.9, 3.2, 2.4, 1.5, 0.8, 0.5
])
TARIFF_KSH_PER_KWH = 25.0   # assumed flat tariff

hours = np.arange(24)
total = energy_kwh.sum()
mean = energy_kwh.mean()
peak_hour = int(np.argmax(energy_kwh))

# Vectorized conversion: every reading becomes a cost in one line
cost_ksh = TARIFF_KSH_PER_KWH * energy_kwh

# Boolean masking: business hours are 08:00-19:59
business = (hours >= 8) & (hours < 20)

print(f"Total energy for the day: {total:.1f} kWh")
print(f"Mean hourly energy: {mean:.2f} kWh")
print(f"Peak hour: {peak_hour}:00 with {energy_kwh[peak_hour]:.1f} kWh")
print(f"Total cost for the day: KSh {cost_ksh.sum():.2f}")
print(f"Share of energy used in business hours: {energy_kwh[business].sum()/total:.1%}")
print("Cost of first six hours (KSh):", cost_ksh[:6])

plt.bar(hours, energy_kwh)
plt.axhline(mean, linestyle="--", color="red", label=f"Mean = {mean:.2f} kWh")
plt.xlabel("Hour of day")
plt.ylabel("Energy used (kWh)")
plt.title("Cyber cafe hourly electricity use")
plt.legend()
plt.grid(True, axis="y")
plt.savefig("figures/Task_02_modified.png", dpi=150, bbox_inches="tight")
plt.show()
