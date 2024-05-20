import pandas as pd
import os
import matplotlib.pyplot as plt

# List to store the counts for each file
counts_list = []


# Iterate through each file in the folder
def plot_data(folder_path, folder_name):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            df = pd.read_csv(f'{folder_path}/{file_name}', delim_whitespace=False, header=None)

            print(df.head())

            # Rename the columns for clarity
            df.columns = ['i', 'x', 'y', 'z']

            # Drop the 'z' column if you don't need it
            df.drop(columns=['z'], inplace=True)
            df.drop(columns=['i'], inplace=True)

            # Convert the DataFrame to a list of lists
            all_points = df.values.tolist()

            x_values = [point[0] for point in all_points]
            y_values = [point[1] for point in all_points]

            plt.plot(x_values, y_values)
            plt.title('Scatter Plot of Points')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.grid(True)
            if not os.path.exists(f'Dataset-Images/{folder_name}'):
                os.makedirs(f'Dataset-Images/{folder_name}')
            output_file_path = os.path.join(f'Dataset-Images/{folder_name}', f'{file_name}')
            plt.savefig(output_file_path)


def store_data(folder_name, folder_path, c):
    plot_data(folder_path, folder_name)
    print(f'{folder_name} done, total completion {round((c / 71) * 100, 2)}%')


# store_data()
folderpath = 'Dataset'
c = 0
for subfolder in os.listdir(folderpath):
    c += 1
    subfolder_path = os.path.join(folderpath, subfolder)
    store_data(subfolder, subfolder_path, c)
