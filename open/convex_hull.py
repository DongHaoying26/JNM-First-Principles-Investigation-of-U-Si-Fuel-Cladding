# -*- coding: utf-8 -*-
"""
U₃Si₂/cladding Interface Reaction Energy Plot
=======================================

Formal plotting script for reaction energies at the U₃Si₂/Fe interface.
Features:
- Lower convex hull with leftmost (0,0) and rightmost (1,0) points as vertices
- Tight axis limits (no extra margins)
- Simplified legend showing only point numbers (#1, #2, ...)
- Enlarged, readable legend in the upper-right corner
- Professional layout suitable for publication

Author: Modified for formal use
Date: March 2026
"""

import numpy as np
import matplotlib.pyplot as plt


# ===================================================================
# USER INPUT SECTION: Reaction data (modify here)
# ===================================================================
# Format: list of dictionaries
# Each entry must contain:
#   - "x":   float (composition fraction, 0.0 to 1.0)
#   - "dH":  float (reaction enthalpy in eV/atom)
#   - "products": list of strings (only for intermediate points)
# End points (x=0 and x=1) must have dH = 0.0 and no "products" key

reactions_data = [
    {"x": 0.0,    "dH": 0.0},
    {"x": x1 data, "dH": dHr data, "products": ['generated phase', 'generated phase']},
    {"x": x2 data, "dH": dHr data, "products": ['generated phase', 'generated phase']},
    {"x": x3 data, "dH": dHr data, "products": ['generated phase', 'generated phase']},
    {"x": x4 data, "dH": dHr data, "products": ['generated phase', 'generated phase']},
    {"x": x5 data, "dH": dHr data, "products": ['generated phase', 'generated phase']},
    {"x": x6 data, "dH": dHr data, "products": ['generated phase', 'generated phase']},
    {"x": 1.0,    "dH": 0.0}
]


# ===================================================================
# Data extraction
# ===================================================================
x = np.array([r["x"] for r in reactions_data])
dH = np.array([r["dH"] for r in reactions_data])


# ===================================================================
# Lower convex hull calculation (forces left and right vertices)
# ===================================================================
def lower_convex_hull(x_vals: np.ndarray, y_vals: np.ndarray) -> np.ndarray:
    """Compute the lower convex hull ensuring (0,0) and (1,0) are vertices."""
    points = list(zip(x_vals, y_vals))
    if len(points) < 2:
        return np.array(points)
    
    lower = []
    for p in points:
        while len(lower) >= 2 and (lower[-1][0] - lower[-2][0]) * (p[1] - lower[-2][1]) - \
                (lower[-1][1] - lower[-2][1]) * (p[0] - lower[-2][0]) <= 0:
            lower.pop()
        lower.append(p)
    return np.array(lower)


hull_points = lower_convex_hull(x, dH)


# ===================================================================
# Plot configuration
# ===================================================================
plt.figure(figsize=(12, 8), dpi=300)

# Marker styles and rainbow colors for visual distinction
markers = ['s', '^', 'D', 'v', 'p', '*', 'h', 'X', 'o']
colors = plt.cm.rainbow(np.linspace(0, 1, len(reactions_data)))

# Plot each reaction point with independent marker
point_handles = []
point_labels = []

for i, (xi, dHi) in enumerate(zip(x, dH)):
    if "products" in reactions_data[i]:
        label = f"#{i}"                                 # Simplified legend
        
        handle = plt.plot(xi, dHi,
                          marker=markers[i % len(markers)],
                          color=colors[i],
                          markersize=10,
                          markeredgecolor='black',
                          markeredgewidth=1.0,
                          linestyle='None',
                          label=label)[0]
        
        point_handles.append(handle)
        point_labels.append(label)


# Plot lower convex hull
plt.plot(hull_points[:, 0], hull_points[:, 1],
         'r--', linewidth=2.5, alpha=0.85, label='Lower Convex Hull')


# ===================================================================
# Axis limits (strictly tight, no extra margins)
# ===================================================================
plt.xlim(-0.005, 1.005)
plt.ylim(min(dH) - 0.05, 0)
plt.margins(x=0, y=0)


# ===================================================================
# Legend (enlarged for better readability)
# ===================================================================
plt.legend(point_handles, point_labels,
           loc='upper right',
           fontsize=11.5,                  # Enlarged label font
           title="Reaction Points",
           title_fontsize=13,               # Enlarged title
           frameon=True,
           framealpha=0.95,
           borderpad=0.8,
           labelspacing=0.4,
           handletextpad=0.6,
           handlelength=1.8,
           ncol=1)


# ===================================================================
# Labels and layout(change 'cladding' to your want)
# ===================================================================
plt.title('U$_3$Si$_2$/cladding Interface Reaction Energies', fontsize=14)
plt.xlabel('x in [xU$_3$Si$_2$ + (1-x)cladding]', fontsize=12)
plt.ylabel('dH$_r$ (eV/atom)', fontsize=12)

plt.xticks([0, 1], ['100% cladding', '100% U$_3$Si$_2$'], fontsize=11)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()


# ===================================================================
# Save and display
# ===================================================================
plt.savefig('U3Si2_cladding_Reaction_Energy_LowerConvexHull_Tight.png',
            dpi=300, bbox_inches='tight')
plt.show()

print("New image generated: U3Si2_cladding_Reaction_Energy_LowerConvexHull_Tight.png")