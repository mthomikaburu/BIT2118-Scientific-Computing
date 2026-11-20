# PageRank for a small 5-page website.
# Links are DIRECTED here (page A links to page B is not the same as B to A).
# The rank vector is the dominant eigenvector (eigenvalue 1) of the Google matrix.
import numpy as np
import matplotlib.pyplot as plt

pages = ["Home", "Courses", "Fees", "Portal", "Contact"]

# links[i] = pages that page i links TO
links = {
    0: [1, 2, 3],      # Home -> Courses, Fees, Portal
    1: [0, 3],         # Courses -> Home, Portal
    2: [0, 3],         # Fees -> Home, Portal
    3: [0],            # Portal -> Home
    4: [0, 3],         # Contact -> Home, Portal (nobody links to Contact)
}
DAMPING = 0.85
n = len(pages)

# Column-stochastic matrix: column j holds the probabilities of leaving page j
M = np.zeros((n, n))
for j, outs in links.items():
    for i in outs:
        M[i, j] = 1 / len(outs)

G = DAMPING * M + (1 - DAMPING) / n * np.ones((n, n))   # Google matrix

# Method 1: eigen-decomposition
eigenvalues, eigenvectors = np.linalg.eig(G)
index = np.argmax(np.real(eigenvalues))
rank_eig = np.abs(np.real(eigenvectors[:, index]))
rank_eig /= rank_eig.sum()

# Method 2: power iteration (what a search engine really does)
rank = np.ones(n) / n
for iteration in range(1, 200):
    new = G @ rank
    change = np.abs(new - rank).sum()
    rank = new
    if change < 1e-12:
        break

print(f"Dominant eigenvalue: {np.real(eigenvalues[index]):.6f}")
print(f"Power iteration stopped after {iteration} iterations")
for i in np.argsort(-rank):
    print(f"{pages[i]:<8} PageRank (eig) = {rank_eig[i]:.4f}   (power iteration) = {rank[i]:.4f}")
print("Both methods agree:", np.allclose(rank, rank_eig))

plt.bar(pages, rank)
plt.ylabel("PageRank score")
plt.title("PageRank of a 5-page website (damping 0.85)")
plt.grid(True, axis="y")
plt.savefig("figures/Task_09_modified.png", dpi=150, bbox_inches="tight")
plt.show()
