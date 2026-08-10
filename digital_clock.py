# digital clock
import time
import tkinter as tk

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(
    root, 
    text="Digital Clock", 
    font=("Arial", 24),
    background="blue",
    foreground="white"
)
clock_label.pack(anchor="center")
root.mainloop()