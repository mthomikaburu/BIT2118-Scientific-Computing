# download speed from a 'total MB downloaded' counter.
# A router logs the total megabytes downloaded every 2 seconds. Speed is the
# derivative of that counter. np.gradient applies central differences for us.
import numpy as np
import matplotlib.pyplot as plt

time_s = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16], dtype=float)
downloaded_mb = np.array([0.0, 3.1, 8.4, 15.9, 24.6, 33.0, 39.2, 42.8, 44.1])

# Central differences inside, one-sided differences at the two ends
speed_mb_s = np.gradient(downloaded_mb, time_s)
speed_mbps = speed_mb_s * 8            # megabytes/s -> megabits/s

# Forward difference for comparison (always "looks ahead" one sample)
forward_mbps = np.diff(downloaded_mb) / np.diff(time_s) * 8

for t, d, v in zip(time_s, downloaded_mb, speed_mbps):
    print(f"t={t:4.0f}s  downloaded={d:5.1f} MB  speed={v:6.2f} Mbps")

peak = np.argmax(speed_mbps)
print(f"Peak speed: {speed_mbps[peak]:.2f} Mbps at t={time_s[peak]:.0f}s")
print(f"Average speed over the whole download: {downloaded_mb[-1]/time_s[-1]*8:.2f} Mbps")
print("Forward-difference speeds (Mbps):", np.round(forward_mbps, 2))

plt.plot(time_s, speed_mbps, marker="o", label="Central difference (np.gradient)")
plt.step(time_s[:-1], forward_mbps, where="post", linestyle="--", label="Forward difference")
plt.xlabel("Time (s)")
plt.ylabel("Download speed (Mbps)")
plt.title("Download speed estimated from the data counter")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_15_modified.png", dpi=150, bbox_inches="tight")
plt.show()
