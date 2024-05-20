import os
import pandas as pd

folderpath = 'Normalized-Dataset'
c = 0

os.makedirs('Normalized Strokes Dataset', exist_ok=True)

for subfolder in os.listdir(folderpath):
    subfolder_path = os.path.join(folderpath, subfolder)
    for i in os.listdir(subfolder_path):
        textfile_path = os.path.join(subfolder_path, i)
        
        # Check if the file is empty
        if os.stat(textfile_path).st_size == 0:
            print(f"Skipping empty file: {textfile_path}")
            continue
        
        try:
            df = pd.read_csv(textfile_path, sep=" ", header=None)
            stroke_indices = df[df[2] == 0].index.tolist()
            stroke_indices.append(len(df))
            strokes = [df.iloc[stroke_indices[i]:stroke_indices[i + 1]] for i in range(len(stroke_indices) - 1)]
            for j, stroke in enumerate(strokes):
                stroke.to_csv(f'Normalized Strokes Dataset/{i.split(".")[0]}_{j + 1}.txt', sep=' ', header=None, index=False)
        except pd.errors.EmptyDataError:
            print(f"EmptyDataError encountered with file: {textfile_path}")
        
    c += 1
    print(f'{subfolder} done, total completion {(c / len(os.listdir(folderpath))) * 100:.2f}%')
