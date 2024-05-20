import tkinter as tk
import pandas as pd
class CharacterDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Character Drawer")

        # Create a canvas to draw on
        self.canvas = tk.Canvas(root, bg="white", width=400, height=400)
        self.canvas.pack()

        # Create a button to clear the canvas
        clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        clear_button.pack()

        # Create a button to save the coordinates
        save_button = tk.Button(root, text="Save", command=self.save_coordinates)
        save_button.pack()

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

        # Initialize drawing variables
        self.drawing = False
        self.last_x = None
        self.last_y = None
        self.coordinates = []

    def start_draw(self, event):
        self.drawing = True
        self.last_x = event.x
        self.last_y = event.y
        self.coordinates.append((event.x, event.y, 0))

    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=2)
            self.last_x = x
            self.last_y = y
            self.coordinates.append((x, y, 1))

    def end_draw(self, event):
        if self.drawing:
            self.drawing = False
            self.coordinates.append((event.x, event.y, 0))

    def clear_canvas(self):
        self.canvas.delete("all")
        self.coordinates = []

    def save_coordinates(self):
        count =0
        print(self.coordinates)
        for i in (self.coordinates):
            for j in i:
                if(i[2]==0):
                    count+=1
        print(count)
        df = pd.DataFrame(self.coordinates)
        df.to_csv('file1.txt', sep='\t', index=False,header=False)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterDrawer(root)
    root.mainloop()
