# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# ====================== Reaction data(such as U3Si2/Fe) ======================
reactions_data = [
    {"x": 0.0,   "dH": 0.0},
    {"x": 0.0571, "dH": -0.2134, "products": ['UFe11Si', 'U3Si']},
    {"x": 0.0667, "dH": -0.2212, "products": ['UFe11Si', 'U2Fe3Si']},
    {"x": 0.1429, "dH": -0.1749, "products": ['U2Fe3Si', 'Fe3Si']},
    {"x": 0.2000, "dH": -0.1970, "products": ['U2Fe3Si', 'UFeSi']},
    {"x": 0.2000, "dH": -0.1992, "products": ['UFeSi', 'UFe2']},
    {"x": 0.2059, "dH": -0.1572, "products": ['U2Fe3Si', 'U3Si5']},
    {"x": 0.2500, "dH": -0.1500, "products": ['U2Fe3Si', 'U3Si']},
    {"x": 0.4000, "dH": -0.1448, "products": ['UFeSi', 'U3Si']},
    {"x": 1.0,   "dH": 0.0}
]

# Extract coordinates
x = np.array([r["x"] for r in reactions_data])
dH = np.array([r["dH"] for r in reactions_data])

# ====================== Custom Lower Convex Hull (Force left and right vertices to be (0,0) and (1,0)) ======================
def lower_convex_hull(x, y):
    points = list(zip(x, y))
    if len(points) < 2:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and (lower[-1][0] - lower[-2][0]) * (p[1] - lower[-2][1]) - \
                (lower[-1][1] - lower[-2][1]) * (p[0] - lower[-2][0]) <= 0:
            lower.pop()
        lower.append(p)
    return np.array(lower)

hull_points = lower_convex_hull(x, dH)

# ====================== Plot Settings ======================
plt.figure(figsize=(12, 8), dpi=300)

# Different shapes + rainbow colors
markers = ['s', '^', 'D', 'v', 'p', '*', 'h', 'X', 'o']
colors = plt.cm.rainbow(np.linspace(0, 1, len(reactions_data)))

# Plot each reaction point (each with independent shape + full legend)
point_handles = []
point_labels = []

for i, (xi, dHi) in enumerate(zip(x, dH)):
    if "products" in reactions_data[i]:
        prod_str = " + ".join(reactions_data[i]["products"])
        label = f"#{i}  {prod_str}"
        
        handle = plt.plot(xi, dHi, 
                          marker=markers[i % len(markers)], 
                          color=colors[i],
                          markersize=12,
                          markeredgecolor='black',
                          markeredgewidth=1.2,
                          linestyle='None',
                          label=label)[0]
        
        point_handles.append(handle)
        point_labels.append(label)

# ====================== Plot Lower Convex Hull (left and right vertices strictly at axis tops) ======================
plt.plot(hull_points[:, 0], hull_points[:, 1], 
         'r--', linewidth=2.5, alpha=0.85, label='Lower Convex Hull')

# ====================== Key Modification: Axes strictly do not exceed data dimensions ======================
plt.xlim(-0.005, 1.005)                    # Left and right exactly fit 100% Fe and 100% U3Si2
plt.ylim(min(dH) - 0.05, 0)                # Upper y-axis limit strictly 0 (no positive value space)
plt.margins(x=0, y=0)                      # Completely remove default margins, so vertices tightly touch the coordinate frame top

# ====================== Legends and Labels ======================
plt.legend(point_handles, point_labels,
           loc='upper right',
           fontsize=10,
           title="Reaction Points",
           title_fontsize=11,
           frameon=True,
           framealpha=0.95,
           borderpad=0.8,
           ncol=1)

plt.title('U$_3$Si$_2$/Fe Interface Reaction Energies', fontsize=14)
plt.xlabel('x in [xU$_3$Si$_2$ + (1-x)Fe]', fontsize=12)
plt.ylabel('dH$_r$ (eV/atom)', fontsize=12)

plt.xticks([0, 1], ['100% Fe', '100% U$_3$Si$_2$'], fontsize=11)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()

plt.savefig('U3Si2_Fe_Reaction_Energy_LowerConvexHull_Tight.png', dpi=300, bbox_inches='tight')
plt.show()

print(" New image generated: U3Si2_Fe_Reaction_Energy_LowerConvexHull_Tight.png")