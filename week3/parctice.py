# HEATMAP
# Problem Statement: Understanding data distribution using a heatmap.
# Question: What areas in the matrix have the highest intensity values?
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = np.random.rand(10,10)  # Generate a 10x10 matrix of random values

# Create heatmap
plt.imshow(data, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title("Heatmap")
plt.show()