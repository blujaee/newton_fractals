import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from main import degree, convergence, iter_counts, rows, cols, max_k

def get_evenly_spaced_colors(n):
    cmap = mpl.colormaps["hsv"]
    evenly_spaced_values = np.linspace(0,0.8,n)
    
    colors = cmap(evenly_spaced_values)
    
    return colors

colors_array = get_evenly_spaced_colors(degree)
rgb = np.zeros((rows,cols,4))
for i in range(rows):
    for j in range(cols):
        if np.isnan(convergence[i,j]):
            rgb[i,j] = [1,0,0,1]
        else:
            brightness = (1 - iter_counts[i,j] / max_k)
            current_color = brightness * colors_array[int(convergence[i,j])]
            rgb[i,j] = current_color

print(colors_array)
plt.imshow(rgb, cmap='hsv', interpolation='nearest')
plt.title("Basins of Convergence")
plt.show()
plt.pause(1)