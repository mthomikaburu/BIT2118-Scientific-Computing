# estimating Kenya's population between census years.
# A census happens only every 10 years. Interpolation estimates the years in between
# (here 2014) from the published census totals.
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Kenya census totals in millions (rounded published figures)
census_year = np.array([1969, 1979, 1989, 1999, 2009, 2019], dtype=float)
population_m = np.array([10.9, 15.3, 21.4, 28.7, 38.6, 47.6])

linear = interp1d(census_year, population_m, kind="linear")
cubic = CubicSpline(census_year, population_m)

for year in (1975, 1994, 2014):
    print(f"{year}: linear = {float(linear(year)):.2f} M   cubic spline = {float(cubic(year)):.2f} M")

# Test the method: hide the 1999 census and try to recover it from the others
keep = census_year != 1999
print(f"Hidden 1999 census (true {population_m[3]} M): "
      f"linear = {float(interp1d(census_year[keep], population_m[keep])(1999)):.2f} M, "
      f"cubic = {float(CubicSpline(census_year[keep], population_m[keep])(1999)):.2f} M")

# Extrapolation (outside the data) is much less trustworthy
print(f"Cubic spline EXTRAPOLATED to 2029: {float(cubic(2029)):.2f} M (treat with caution)")

years = np.arange(1969, 2020)
plt.scatter(census_year, population_m, label="Census totals", zorder=3)
plt.plot(years, linear(years), label="Linear")
plt.plot(years, cubic(years), linestyle="--", label="Cubic spline")
plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.title("Kenya population between census years")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_13_modified.png", dpi=150, bbox_inches="tight")
plt.show()
