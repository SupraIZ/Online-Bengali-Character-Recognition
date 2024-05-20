import pandas as pd
import os
from collections import Counter

# List to store the counts for each file
counts_list = []


# Iterate through each file in the folder
def optimal_number(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            # Read the file into a DataFrame
            df = pd.read_csv(file_path, header=None, names=['x', 'y', 'z'], delimiter=' ')
            # Count occurrences of '0' in the 'z' column and append to the list
            counts_list.append(df['z'].value_counts().get(0, 0))

    # Print or use the counts_list as needed
    counter = Counter(counts_list)

    # Use the most_common(1) method to get the most common element
    res = counter.most_common(1)[0][0]
    return res


def store_data(folder_name, folder_path, c):
    most_common_elem = optimal_number(folder_path)
    stra = f'{folder_name}: {most_common_elem}'
    file_path = 'output.txt'
    with open(file_path, 'a') as file:
        file.write(stra + '\n')
    print(f'{folder_name} done, total completion {(c / 71) * 100}%')


# store_data()
folderpath = 'Dataset'
c = 0
for subfolder in os.listdir(folderpath):
    c += 1
    subfolder_path = os.path.join(folderpath, subfolder)
    store_data(subfolder, subfolder_path, c)
