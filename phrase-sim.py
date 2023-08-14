import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Load the first .npy file (3x1536 array)
array1 = np.load('phrase.npy')

# Load the second .npy file (mx1536 array)
array2 = np.load('emoji-embeddings.npy')

# Compute cosine similarity between rows
cosine_sim_matrix = cosine_similarity(array1, array2)

# Transpose the similarity matrix for plotting
cosine_sim_matrix = cosine_sim_matrix

# Save the cosine similarity matrix as .npy file
np.save('cosine_sim_matrix.npy', cosine_sim_matrix)

average_delta = np.mean(cosine_sim_matrix, axis=1)

# Calculate the delta between consecutive elements along axis 1
delta_array = np.diff(cosine_sim_matrix, axis=1)

# Calculate the average delta along the long dimension (axis 0)
average_delta = np.mean(delta_array, axis=0)

# Plot the average delta values
plt.plot(average_delta)
plt.title('Average Delta along the Long Dimension')
plt.xlabel('Column')
plt.ylabel('Average Delta')
plt.show()

num_rows, num_columns = cosine_sim_matrix.shape
print(cosine_sim_matrix.shape)
# Plot the cosine similarity matrix
for row_index in range(num_rows):
    plt.figure()
    plt.plot(cosine_sim_matrix[row_index])
    print(cosine_sim_matrix[row_index][0])
    plt.title(f'Row {row_index + 1}')
    plt.xlabel('Column')
    plt.ylabel('Value')
    plt.show()