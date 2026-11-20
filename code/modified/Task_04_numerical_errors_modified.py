# round-off error building up in a billing system.
# A system adds KSh 0.10 to a running total one million times. The exact answer is
# KSh 100,000. We see how far float32 and float64 drift, and how to avoid it.
import math
from decimal import Decimal
import numpy as np

N = 1_000_000
STEP = 0.10
exact = 100_000.0

total32 = np.float32(0.0)
total64 = 0.0
for _ in range(N):
    total32 += np.float32(STEP)
    total64 += STEP

total_fsum = math.fsum([STEP] * N)                      # compensated summation
total_decimal = sum([Decimal("0.10")] * N, Decimal(0))  # exact decimal arithmetic
total_cents = (10 * N) / 100                            # store money as integer cents

def report(label, value):
    abs_err = abs(float(value) - exact)
    print(f"{label:<22} total = {float(value):>16.6f}   abs error = {abs_err:.6e}   rel error = {abs_err/exact:.3e}")

report("float32 running sum", total32)
report("float64 running sum", total64)
report("math.fsum", total_fsum)
report("Decimal", total_decimal)
report("integer cents", total_cents)
print("float64 total == 100000.0 ?", total64 == exact)
print("np.isclose(float64 total, 100000.0) ?", np.isclose(total64, exact))
