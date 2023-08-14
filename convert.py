import numpy as np

# Load the numpy array from the .npy file
arr = np.load('phrase-emoji-sim.npy')

csv_text = np.savetxt("phrase-emoji-sim.txt", arr, delimiter=",", fmt='%s')

with open("phrase-emoji-sim.txt", 'r') as f:
    csv_content = f.read()
    
from io import StringIO

# Convert CSV text back to numpy array
csv_file = StringIO(csv_content)
loaded_arr = np.loadtxt(csv_file, delimiter=",")

print(loaded_arr[1][1]);