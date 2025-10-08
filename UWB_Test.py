import numpy as np

def trilaterate_xy(ref_points, distances, z_known):
    refs = np.array(ref_points, dtype=float)
    d = np.array(distances, dtype=float)

    if refs.shape != (3, 3):
        raise ValueError("ref_points must be shape (3,3)")

    # Step 1: horizontal distances after subtracting vertical offset
    dz = z_known - refs[:, 2]
    h2 = d**2 - dz**2

    if np.any(h2 < -1e-9):  # allow tiny numerical negatives
        raise ValueError("Inconsistent distances and height (no real solution)")

    h2 = np.clip(h2, 0, None)  # avoid negative due to rounding

    # Step 2: build linear system from circle differences
    x1, y1 = refs[0, :2]
    eqs = []
    rhs = []
    for j in [1, 2]:
        xj, yj = refs[j, :2]
        Arow = [2*(x1 - xj), 2*(y1 - yj)]
        bval = h2[0] - h2[j] + xj**2 - x1**2 + yj**2 - y1**2
        eqs.append(Arow)
        rhs.append(bval)

    A = np.array(eqs)
    b = np.array(rhs)

    # Step 3: solve 2x2 system (or least squares if degenerate)
    if np.linalg.matrix_rank(A) == 2:
        xy = np.linalg.solve(A, b)
    else:
        xy, *_ = np.linalg.lstsq(A, b, rcond=None)

    return tuple(xy)

ref_points = [
    (0.0, 0.0, 0.0),        # Corner
    (0.33, 0.0, 0.0),       # X-Axis
    (0.0, 0.33, 0.0)        # Y-Axis
]

# Unknown point is at (4, 3, 2)
true_point = (4.0, 3.0, 2.0)
dists = [np.linalg.norm(np.array(true_point) - np.array(p)) for p in ref_points]

xy_est = trilaterate_xy(ref_points, dists, z_known=5)
print("Estimated (x, y):", xy_est)