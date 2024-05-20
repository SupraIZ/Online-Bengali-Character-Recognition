import os
import numpy as np

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            parts = line.strip().split()
            if len(parts) == 3:
                try:
                    data.append([float(parts[0]), float(parts[1]), int(parts[2])])
                except ValueError:
                    print(f"Skipping invalid line in {file_path}: {line.strip()}")
            else:
                print(f"Skipping malformed line in {file_path}: {line.strip()}")
    return np.array(data)

def normalize_coordinates(coordinates, target_size=64):
    if len(coordinates) == 0:
        return coordinates

    x = coordinates[:, 0]
    y = coordinates[:, 1]

    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)

    if max_x == min_x:
        max_x = min_x + 1  # Avoid division by zero
    if max_y == min_y:
        max_y = min_y + 1  # Avoid division by zero

    # Normalize x and y to the range [0, target_size-1]
    x_normalized = ((x - min_x) / (max_x - min_x)) * (target_size - 1)
    y_normalized = ((y - min_y) / (max_y - min_y)) * (target_size - 1)

    normalized_coordinates = np.column_stack((x_normalized, y_normalized, coordinates[:, 2]))
    return normalized_coordinates

def save_normalized_data(coordinates, original_file_path, output_directory):
    relative_path = os.path.relpath(original_file_path, start=main_directory)
    new_file_path = os.path.join(output_directory, relative_path)
    os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
    np.savetxt(new_file_path, coordinates, fmt='%.6f %.6f %d')

def normalize_dataset(main_directory, output_directory, target_size=64):
    for root, dirs, files in os.walk(main_directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                coordinates = load_data(file_path)
                normalized_coordinates = normalize_coordinates(coordinates, target_size)
                save_normalized_data(normalized_coordinates, file_path, output_directory)

if __name__ == "__main__":
    main_directory = 'Dataset'
    output_directory = 'Normalized-Dataset'
    normalize_dataset(main_directory, output_directory)
