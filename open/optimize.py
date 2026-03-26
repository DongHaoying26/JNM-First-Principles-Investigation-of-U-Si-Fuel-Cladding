import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define data
compounds_data = [
    {"U": 0.95, "MAE": -89.302876},
    {"U": 0.96, "MAE": -89.747984},
    {"U": 0.97, "MAE": -90.018991},
    {"U": 0.98, "MAE": -90.130493},
    {"U": 0.99, "MAE": -90.103014},
    {"U": 1.00, "MAE": -89.965864},
    {"U": 1.01, "MAE": -89.722148},
    {"U": 1.02, "MAE": -89.395432},
    {"U": 1.03, "MAE": -88.990979},
    {"U": 1.04, "MAE": -88.522761},
    {"U": 1.05, "MAE": -87.992502},
]

# Extract data
U_values = [data["U"] for data in compounds_data]
MAE_values = [data["MAE"] for data in compounds_data]

# Use spline interpolation
U_smooth = np.linspace(min(U_values), max(U_values), 1000)
spl = make_interp_spline(U_values, MAE_values, k=3)
MAE_smooth = spl(U_smooth)

# Plot original data
plt.scatter(U_values, MAE_values, label='Original Data')

# Plot smooth curve
plt.plot(U_smooth, MAE_smooth, label='Smooth Curve', color='red')

# Get the index of the minimum value of the fitted curve
min_index = np.argmin(MAE_smooth)

# Get the U and MAE corresponding to the minimum value
min_U = round(U_smooth[min_index], 4)
min_MAE = round(MAE_smooth[min_index], 4)

# Mark the minimum point
plt.scatter(min_U, min_MAE, color='green', label=f'Min MAE ({min_U}, {min_MAE})')

plt.xlabel('x')
plt.ylabel('E')
plt.title('fdxs-E Smooth Curve Fitting')
plt.legend()
# Save the image to the same directory
plt.savefig('smooth_fit_curve_plot.png')

plt.show()
