import pandas as pd
import os
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


# Function to load and prepare data from multiple CSV files
def load_data_from_csv(folder_path):
    data = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)
                df = pd.read_csv(file_path)
                if not df.empty:  # Check if DataFrame is not empty
                    data.append(df[['x', 'y']].values)
    return data


# Function to apply K-means clustering
def apply_kmeans(data, num_clusters):
    if data:  # Check if data is not empty
        flattened_data = np.concatenate(data)  # Flatten the list of arrays into a single array
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(flattened_data)
        return kmeans.labels_
    else:
        print("No valid data found for clustering.")
        return None


# Main function to cluster Bengali characters from CSV files in subfolders
def cluster_bengali_characters(folderpath, num_clusters):
    data = load_data_from_csv(folderpath)

    labels = apply_kmeans(data, num_clusters)

    if labels is not None:
        # Visualize clusters
        plt.figure(figsize=(8, 6))
        for i in range(num_clusters):
            cluster_points = [point for j, point in enumerate(np.concatenate(data)) if labels[j] == i]
            cluster_points = np.array(cluster_points)
            plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i + 1}')

        plt.title('K-means Clustering of Bengali Characters')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.show()


# Define the number of clusters
num_clusters = 3

# Call the function to convert text files to CSV files for Bengali characters
def load_data_from_files(folder_path):
    c = 1
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            new_dir = os.path.join('Output_Directory', dir)
            os.makedirs(new_dir, exist_ok=True)
            for filename in os.listdir(os.path.join(folder_path, dir)):
                if filename.endswith(".txt"):
                    file_path = os.path.join(folder_path, dir, filename)
                    df = pd.read_csv(file_path, header=None, names=['x', 'y', 'z'], delimiter=' ')
                    output_file = os.path.join(new_dir, filename.replace('.txt', '.csv'))
                    df.to_csv(output_file, index=False)
        # print(f'{folder_path} done, total completion {round((c / 71) * 100, 2)}%')
        # c+=1


# Define the folder path containing text files for Bengali characters
folder_path = 'New folder (2)'

# Load and save data from multiple text files to new directories as CSV files
load_data_from_files(folder_path)

# Call the main function to cluster Bengali characters from CSV files in subfolders
cluster_bengali_characters('Output_Directory', num_clusters)