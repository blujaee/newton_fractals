import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from main import run

def get_evenly_spaced_colors(n):
    cmap = mpl.colormaps["hsv"]
    evenly_spaced_values = np.linspace(0, 0.8, n)
    return cmap(evenly_spaced_values)

def plot_fractal(convergence, iter_counts, rows, cols, max_k, roots):
    colors_array = get_evenly_spaced_colors(len(roots))
    rgb = np.zeros((rows, cols, 4))
    for i in range(rows):
        for j in range(cols):
            if np.isnan(convergence[i, j]):
                rgb[i, j] = [1, 0, 0, 1]
            else:
                brightness = 1 - np.log1p(iter_counts[i, j]) / np.log1p(max_k)
                current_color = colors_array[int(convergence[i, j])].copy()
                current_color[:3] *= brightness
                rgb[i, j] = current_color

    plt.imshow(rgb, interpolation='nearest')
    plt.title("Basins of Attraction")
    plt.show()

if __name__ == "__main__":
    convergence, iter_counts, rows, cols, max_k, roots = run()
    plot_fractal(convergence, iter_counts, rows, cols, max_k, roots)
