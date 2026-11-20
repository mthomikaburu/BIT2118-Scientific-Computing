# moving a triangular game sprite.
# The original only rotated and scaled. Here we also TRANSLATE (move) the shape,
# which needs 3x3 homogeneous matrices. Order: scale -> rotate -> translate.
import numpy as np
import matplotlib.pyplot as plt

# Triangle sprite: each row is [x, y]
points = np.array([
    [0.0, 0.0],
    [2.0, 0.0],
    [1.0, 1.5]
])

angle = np.deg2rad(30)
sx, sy = 1.5, 1.5        # uniform scaling
tx, ty = 4.0, 2.0        # move 4 right, 2 up

S = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
R = np.array([[np.cos(angle), -np.sin(angle), 0],
              [np.sin(angle),  np.cos(angle), 0],
              [0, 0, 1]])
T = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])

M = T @ R @ S            # the rightmost matrix is applied first

# Add a column of ones -> homogeneous coordinates [x, y, 1]
homogeneous = np.hstack([points, np.ones((len(points), 1))])
transformed = (homogeneous @ M.T)[:, :2]

def area(p):
    (x1, y1), (x2, y2), (x3, y3) = p
    return 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

np.set_printoptions(precision=4, suppress=True)
print("Combined matrix M = T @ R @ S:\n", M)
print("Original points:\n", points)
print("Transformed points:\n", transformed)
print(f"Determinant of the 2x2 linear part: {np.linalg.det(M[:2, :2]):.4f}")
print(f"Original area: {area(points):.4f}   Transformed area: {area(transformed):.4f}")
back = (np.hstack([transformed, np.ones((3, 1))]) @ np.linalg.inv(M).T)[:, :2]
print("Inverse matrix recovers the original points:", np.allclose(back, points))

for p, label in [(points, "Original"), (transformed, "Transformed")]:
    closed = np.vstack([p, p[0]])
    plt.plot(closed[:, 0], closed[:, 1], marker="o", label=label)
plt.axis("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sprite scaled x1.5, rotated 30 deg, moved (4, 2)")
plt.legend()
plt.grid(True)
plt.savefig("figures/Task_05_modified.png", dpi=150, bbox_inches="tight")
plt.show()
