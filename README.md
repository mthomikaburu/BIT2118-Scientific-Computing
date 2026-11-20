# BIT 2118: Scientific Computing - Group 6

**Group members:**

| No. | Name | Reg. No. |
|---|---|---|
| 1 | Stephen Kimani | BSCCS/2024/57444 |
| 2 | Oscar Munene | BSCCS/2025/34405 |
| 3 | Allan Mwaura | BSCCS/2024/59744 |
| 4 | Caleb Wakahua | BSCCS/2024/49983 |
| 5 | Rachael Maina | BSCCS/2025/34548 |
| 6 | Zacharia Kimani | BSCCS/2024/60395 |
| 7 | Kaburu Evans Muthomi | BSCCS/2024/62210 |
| 8 | Maureen Wairimu | BSCCS/2025/68877 |
| 9 | Maxwell Waime | BSCCS/2024/59239 |
| 10 | Carolyne Situma | BSCCS/2024/53028 |

This repository holds our group's work on the BIT 2118 tasks (Tasks 2 to 20). For every task we ran the handout program, identified its inputs and mathematical operation, changed one input and explained the effect, explained the output and graph, and then wrote a modified program for a different but related real-world case.

**Full write-up: [docs/DOCUMENTATION.md](docs/DOCUMENTATION.md)**

## What is in this repository

| Folder | Contents |
|---|---|
| `code/original/` | The 19 handout programs (Instructions B and D) |
| `code/changed/` | The same programs with one input/parameter changed (Instruction C) |
| `code/modified/` | Our programs for a different real-world case (Instruction E) |
| `outputs/` | Printed output of every program, saved as text |
| `figures/` | Every graph, saved as PNG |
| `docs/` | The documentation for all tasks |

## Tasks and our modified cases

| Task | Concept | Handout case | Our modified case (Instruction E) |
|---|---|---|---|
| 2 | NumPy arrays | Weather-station temperatures | Hourly electricity use and cost of a cyber cafe |
| 3 | Vectorization | Network latency conversion | Fees on one million mobile-money transactions |
| 4 | Floating-point errors | 0.1 + 0.2 and sqrt(2) | Round-off building up in a billing total |
| 5 | Matrix algebra | Rotate and scale a square | Scale, rotate and move a game sprite (3x3 matrices) |
| 6 | Linear systems | Two server types | Three vehicle types run by a SACCO |
| 7 | Gaussian elimination and LU | Repeated measurement vectors | Loop currents in a DC circuit |
| 8 | Iterative methods | Temperatures on a grid | Output needed from four linked business units |
| 9 | Eigenvalues and eigenvectors | Node importance in a network | PageRank of a 5-page website |
| 10 | Bisection and fixed-point | Heat-balance temperature | Break-even point of a T-shirt business |
| 11 | Newton-Raphson and secant | Internal rate of return | Hidden interest rate on a hire-purchase phone |
| 12 | Nonlinear equations | Circle meets parabola | Locating a phone from cell towers; a falling ball |
| 13 | Interpolation | Temperature every 10 minutes | Kenya's population between census years |
| 14 | Curve fitting | Server response time | Exponential growth of app users |
| 15 | Numerical differentiation | Speed from GPS positions | Download speed from a data counter |
| 16 | Numerical integration | Energy from smart-meter power | Distance covered by a matatu |
| 17 | Euler method | Cooling of a hot object | Tilapia growth in a fish pond (logistic) |
| 18 | ODEs with SciPy | RC circuit charging | Flu spreading on a campus (SIR model) |
| 19 | Optimization | Cheapest server allocation | Cheapest chicken-feed mix |
| 20 | Monte Carlo | Server overload risk | Chance of being late for an 8 am class |

## How to run

```bash
pip install -r requirements.txt

# run one program (always from the repository root, so figures save to figures/)
python code/original/Task_08_iterative_linear.py
python code/changed/Task_08_iterative_linear_changed.py
python code/modified/Task_08_iterative_linear_modified.py
```

Tested with Python 3, NumPy 2.x, SciPy 1.x and Matplotlib 3.x. NumPy 2.0 or newer is needed because Task 16 uses `np.trapezoid`.

## Small differences from the handout code

- Programs with graphs also save the graph with `plt.savefig(...)` before `plt.show()`.
- Tasks 8, 11 and 17 print a few extra lines (iteration counts, largest error) that are used in the explanations.
- Task 13 builds the 10-minute time grid with `np.linspace(8, 14, 37)` instead of `np.arange(8, 14 + 1/6, 1/6)`, because `arange` with a fractional step can produce a value slightly above 14, which `interp1d` rejects as out of range.
- Task 19 stores the required capacity in one constant so that it can be changed in one place.
