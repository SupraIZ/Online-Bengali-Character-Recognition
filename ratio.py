import os
import pandas as pd
import numpy as np

# Function to calculate ratios for a single file
def calculate_ratios(file_path):
    df = pd.read_csv(file_path, sep=" ", header=None, names=['x', 'y', 'stroke'])
    # Calculate x and y ratios
    x_ratio = (df['x'].max() - df['x'].min()) / len(df)
    y_ratio = (df['y'].max() - df['y'].min()) / len(df)
    # Calculate width and height
    width = df['x'].max() - df['x'].min()
    height = df['y'].max() - df['y'].min()
    num_strokes = df['stroke'].max() + 1  # Assuming strokes are zero-indexed
    width_ratio = width / num_strokes
    height_ratio = height / num_strokes
    return x_ratio, y_ratio, width_ratio, height_ratio

# Main function to process all files and calculate average ratios per character
def calculate_character_ratios(normalized_dataset_folder, output_file):
    character_ratios = {}
    total_characters = len(os.listdir(normalized_dataset_folder))
    character_count = 0

    for character in os.listdir(normalized_dataset_folder):
        character_folder_path = os.path.join(normalized_dataset_folder, character)
        if os.path.isdir(character_folder_path):
            x_ratios = []
            y_ratios = []
            width_ratios = []
            height_ratios = []
            file_count = 0
            total_files = len(os.listdir(character_folder_path))
            
            for file in os.listdir(character_folder_path):
                file_path = os.path.join(character_folder_path, file)
                if os.path.isfile(file_path):
                    try:
                        x_ratio, y_ratio, width_ratio, height_ratio = calculate_ratios(file_path)
                        x_ratios.append(x_ratio)
                        y_ratios.append(y_ratio)
                        width_ratios.append(width_ratio)
                        height_ratios.append(height_ratio)
                        file_count += 1
                        print(f"Processed file {file_count}/{total_files} in {character} folder")
                    except Exception as e:
                        print(f"Error processing file {file_path}: {e}")

            if x_ratios and y_ratios and width_ratios and height_ratios:
                average_x_ratio = np.mean(x_ratios)
                average_y_ratio = np.mean(y_ratios)
                average_width_ratio = np.mean(width_ratios)
                average_height_ratio = np.mean(height_ratios)
                character_ratios[character] = (average_x_ratio, average_y_ratio, average_width_ratio, average_height_ratio)
            character_count += 1
            print(f"Completed processing {character} ({character_count}/{total_characters})")

    # Save the results to a CSV file
    with open(output_file, 'w') as f:
        f.write('Character,Average X Ratio,Average Y Ratio,Average Width Ratio,Average Height Ratio\n')
        for character, ratios in character_ratios.items():
            f.write(f'{character},{ratios[0]},{ratios[1]},{ratios[2]},{ratios[3]}\n')

if __name__ == "__main__":
    normalized_dataset_folder = 'Normalized Strokes Dataset'
    output_file = 'character_ratios.csv'
    calculate_character_ratios(normalized_dataset_folder, output_file)
    print(f"Character ratios have been calculated and saved to {output_file}")
