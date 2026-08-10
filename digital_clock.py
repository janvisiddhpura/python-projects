# digital clock
import time
import tkinter as tk

root = tk.Tk()
root.title("Digital Clock")

def current_time():
    # current time in hours, minutes and seconds and displays on the clock
    time_string = time.strftime("%A, %b %d \n\n %I:%M:%S %p")
    clock_label.config(text=time_string)
    # update the time in every 1000 ms
    clock_label.after(1000, current_time)

clock_label = tk.Label(
    root, 
    text="Digital Clock", 
    font=("Arial", 24),
    background="black",
    foreground="pale green"
)
clock_label.pack(anchor="center")
current_time()
root.mainloop()