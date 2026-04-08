import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from main import run

PALETTE = [
    [1.00, 0.41, 0.71, 1],  # hot pink
    [0.80, 0.60, 1.00, 1],  # lavender
    [1.00, 0.08, 0.58, 1],  # deep rose
    [0.96, 0.76, 0.86, 1],  # baby pink
    [0.69, 0.40, 0.82, 1],  # purple
    [1.00, 0.60, 0.80, 1],  # light pink
    [0.55, 0.20, 0.60, 1],  # dark purple
    [1.00, 0.75, 0.80, 1],  # blush
]

def get_evenly_spaced_colors(n):
    colors = [PALETTE[i % len(PALETTE)] for i in range(n)]
    return np.array(colors)

def plot_fractal(convergence, iter_counts, rows, cols, max_k, roots):
    colors_array = get_evenly_spaced_colors(len(roots))
    rgb = np.zeros((rows, cols, 4))
    for i in range(rows):
        for j in range(cols):
            if np.isnan(convergence[i, j]):
                rgb[i, j] = [0.15, 0.05, 0.20, 1]  # deep plum for non-converged
            else:
                brightness = 0.35 + 0.65 * (1 - np.log1p(iter_counts[i, j]) / np.log1p(max_k))
                current_color = colors_array[int(convergence[i, j])].copy()
                current_color[:3] *= brightness
                rgb[i, j] = current_color

    plt.imshow(rgb, interpolation='nearest')
    plt.title("Basins of Attraction")
    plt.show()

if __name__ == "__main__":
    convergence, iter_counts, rows, cols, max_k, roots = run()
    plot_fractal(convergence, iter_counts, rows, cols, max_k, roots)
