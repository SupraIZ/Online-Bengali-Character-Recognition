import pandas as pd
import os
import matplotlib.pyplot as plt

# Function to plot data
def plot_data(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            df = pd.read_csv(f'{folder_path}/{file_name}', delim_whitespace=True, header=None, names=['x', 'y', 'z'])

            plt.figure(figsize=(2, 2))  # Ensure the aspect ratio is 1:1
            plt.plot(df['x'], df['y'])
            plt.title(file_name)
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.xlim(0, 64)
            plt.ylim(0, 64)
            plt.gca().invert_yaxis()  # Invert Y axis for correct orientation
            plt.grid(True)
            plt.axis('equal')

            if not os.path.exists('Strokes-Images'):
                os.makedirs('Strokes-Images')
            output_file_path = os.path.join('Strokes-Images', file_name.replace('.txt', '.png'))
            plt.savefig(output_file_path, format='png')
            plt.close()

# Plot data
folderpath = 'Normalized Strokes Dataset'
plot_data(folderpath)
