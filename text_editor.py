# creating a text editor using tkinter
import tkinter as tk
from tkinter import filedialog, messagebox

# main window structure
root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

# create textarea
text_area = tk.Text(
    root, 
    wrap=tk.WORD, 
    font=("Arial", 12)
)
text_area.pack(expand=True, fill=tk.BOTH)

# create a new file
def new_file():
    text_area.delete(1.0, tk.END)
    
# initiates and keep the window open until user closes it
root.mainloop()
