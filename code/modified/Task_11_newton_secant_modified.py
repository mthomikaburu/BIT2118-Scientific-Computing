# the hidden interest rate on a hire-purchase phone.
# Cash price KSh 20,000, or 12 monthly instalments of KSh 2,100.
# The monthly rate r solves  f(r) = A*(1-(1+r)^-n)/r - P = 0.
# Newton-Raphson and Secant are written out by hand to show each iteration.

P = 20_000.0   # cash price (the amount effectively borrowed)
A = 2_100.0    # monthly instalment
n = 12         # number of instalments

def f(r):
    return A * (1 - (1 + r)**-n) / r - P

def df(r):
    return A * (n * r * (1 + r)**(-n - 1) - (1 - (1 + r)**-n)) / r**2

print("Newton-Raphson")
r = 0.05
for i in range(1, 50):
    r_new = r - f(r) / df(r)
    print(f"  iteration {i}: r = {r_new:.10f}")
    if abs(r_new - r) < 1e-12:
        break
    r = r_new
newton_root, newton_iters = r_new, i

print("Secant")
r0, r1 = 0.01, 0.05
for i in range(1, 50):
    r2 = r1 - f(r1) * (r1 - r0) / (f(r1) - f(r0))
    print(f"  iteration {i}: r = {r2:.10f}")
    if abs(r2 - r1) < 1e-12:
        break
    r0, r1 = r1, r2
secant_root, secant_iters = r2, i

print(f"Monthly rate (Newton): {newton_root:.4%} in {newton_iters} iterations")
print(f"Monthly rate (Secant): {secant_root:.4%} in {secant_iters} iterations")
print(f"Check f(root) = {f(newton_root):.2e}")
print(f"Nominal annual rate (12 x monthly): {12*newton_root:.2%}")
print(f"Effective annual rate: {(1+newton_root)**12 - 1:.2%}")
print(f"Total paid: KSh {A*n:,.0f}   Extra over cash price: KSh {A*n - P:,.0f}")
