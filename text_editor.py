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

# open an existing file
def open_file():
    # open file dialog to select a file
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        # open the file and read its content
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
    
# initiates and keep the window open until user closes it
root.mainloop()
