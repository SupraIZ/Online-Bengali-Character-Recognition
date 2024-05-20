import os
import pandas as pd

folderpath = 'Optimal Extracted Stroke'
c = 0

os.makedirs('Optimal Strokes Dataset', exist_ok=True)

for subfolder in os.listdir(folderpath):
    subfolder_path = os.path.join(folderpath, subfolder)
    for i in os.listdir(subfolder_path):
        textfile_path = os.path.join(subfolder_path, i)
        df = pd.read_csv(textfile_path, sep=" ", header=None)
        stroke_indices = df[df[2] == 0].index.tolist()
        stroke_indices.append(len(df))
        strokes = [df.iloc[stroke_indices[i]:stroke_indices[i + 1]] for i in range(len(stroke_indices) - 1)]
        for j, stroke in enumerate(strokes):
            stroke_output_path = os.path.join('Optimal Strokes Dataset', f'{i.split(".")[0]}_{j + 1}.txt')
            stroke.to_csv(stroke_output_path, sep=' ', header=None, index=False)
    c += 1
    print(f'{subfolder} done, total completion {(c / len(os.listdir(folderpath))) * 100:.2f}%')
