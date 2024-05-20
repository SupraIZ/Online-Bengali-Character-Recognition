import os
import pandas as pd
from collections import Counter

def optimal_number_and_extract_stroke(folder_path, output_folder):
    counts_list = []
    file_paths = []
    
    # Iterate through files and collect stroke counts and file paths
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path, header=None, names=['x', 'y', 'z'], delimiter=' ')
            stroke_count = df['z'].value_counts().get(0, 0)
            counts_list.append(stroke_count)
            file_paths.append(file_path)
    
    # Determine the most common stroke count
    counter = Counter(counts_list)
    most_common_stroke_count = counter.most_common(1)[0][0]
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Extract and save the first file with the most common stroke count
    for i, stroke_count in enumerate(counts_list):
        if stroke_count == most_common_stroke_count:
            output_file_path = os.path.join(output_folder, os.path.basename(file_paths[i]))
            df = pd.read_csv(file_paths[i], header=None, names=['x', 'y', 'z'], delimiter=' ')
            df.to_csv(output_file_path, sep=' ', header=False, index=False)
            break  # Stop after saving the first optimal stroke file

    return most_common_stroke_count

def store_optimal_data(folder_path, output_folder):
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            subfolder_output_path = os.path.join(output_folder, subfolder)
            most_common_stroke_count = optimal_number_and_extract_stroke(subfolder_path, subfolder_output_path)
            print(f'{subfolder}: Optimal stroke count = {most_common_stroke_count}')

# Main execution
folderpath = 'Normalized-Dataset'
output_folder = 'Optimal Extracted Stroke'
store_optimal_data(folderpath, output_folder)
