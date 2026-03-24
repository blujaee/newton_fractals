from main import scaled_convergence, iter_counts
import matplotlib.pyplot as plt
import matplotlib.colors as clr

plt.imshow(scaled_convergence, cmap='viridis', interpolation='nearest')
plt.title("Basins of Convergence")
plt.show()
plt.pause(1)