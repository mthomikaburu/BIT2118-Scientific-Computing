# fees on one million mobile-money transactions.
# Each transaction pays a 0.5% fee capped at KSh 100. We compute all fees with a
# Python loop and with vectorized NumPy, and compare the time.
import numpy as np
import timeit

rng = np.random.default_rng(7)
amounts_ksh = rng.uniform(50, 70_000, 1_000_000)   # simulated transaction amounts

FEE_RATE = 0.005
FEE_CAP = 100.0

def loop_version():
    fees = []
    for amount in amounts_ksh:
        fees.append(min(amount * FEE_RATE, FEE_CAP))
    return fees

def vectorized_version():
    return np.minimum(amounts_ksh * FEE_RATE, FEE_CAP)

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

fees = vectorized_version()

print("First five fees (KSh):", np.round(fees[:5], 2))
print(f"Total fees collected: KSh {fees.sum():,.2f}")
print(f"Transactions hitting the KSh 100 cap: {(fees == FEE_CAP).mean():.1%}")
print("Loop and vectorized results agree:", np.allclose(loop_version(), fees))
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")
