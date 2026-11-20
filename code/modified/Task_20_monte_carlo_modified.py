# will a student be late for an 8:00 am class?
# A Thika -> Nairobi commute has three uncertain parts. We simulate 100,000
# mornings and estimate the probability that the trip takes more than 90 minutes.
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
N = 100_000
TIME_AVAILABLE = 90.0    # minutes between leaving home and the start of class

# Assumed distributions (minutes)
wait_for_matatu = rng.uniform(2, 15, N)                 # waiting for it to fill
highway_drive = rng.normal(45, 8, N)                    # Thika Road drive
jam_delay = np.where(rng.random(N) < 0.25,              # 25% of mornings: a jam
                     rng.exponential(20, N), 0.0)
walk_to_class = rng.triangular(8, 10, 15, N)            # stage to lecture hall

total = wait_for_matatu + highway_drive + jam_delay + walk_to_class
late = total > TIME_AVAILABLE
p_late = late.mean()
standard_error = np.sqrt(p_late * (1 - p_late) / N)

print(f"Mean commute time: {total.mean():.1f} min   Standard deviation: {total.std():.1f} min")
print(f"Estimated probability of being late: {p_late:.2%}")
print(f"95% confidence interval: {p_late - 1.96*standard_error:.2%} to {p_late + 1.96*standard_error:.2%}")
print(f"Late mornings: {late.sum()} out of {N}")
print(f"Time to allow to be on time 95% of mornings: {np.percentile(total, 95):.1f} min")
print(f"Probability of being late if there is no jam: {late[jam_delay == 0].mean():.2%}")
print(f"Probability of being late if there is a jam:  {late[jam_delay > 0].mean():.2%}")

running = np.cumsum(late) / np.arange(1, N + 1)
indices = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
ax1.hist(total, bins=80)
ax1.axvline(TIME_AVAILABLE, color="red", linestyle="--", label="90 min available")
ax1.set_xlabel("Total commute time (min)")
ax1.set_ylabel("Number of simulated mornings")
ax1.set_title("Distribution of commute time")
ax1.legend()
ax2.semilogx(indices + 1, running[indices])
ax2.set_xlabel("Number of simulations")
ax2.set_ylabel("Estimated probability of being late")
ax2.set_title("Convergence of the estimate")
ax2.grid(True)
plt.savefig("figures/Task_20_modified.png", dpi=150, bbox_inches="tight")
plt.show()
