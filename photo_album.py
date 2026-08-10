# slideshow of images using tkinter and PIL
import tkinter as tk
import time
from PIL import Image, ImageTk

# main window structure
root = tk.Tk()
root.title("Photo Slideshow")
root.geometry("900x900")
root.configure(bg="black")

# list of image paths
image_paths = [
    r"C:\Users\Admin\Downloads\image1.jpg",
    r"C:\Users\Admin\Downloads\image2.jpg",
    r"C:\Users\Admin\Downloads\image3.jpg",
    r"C:\Users\Admin\Downloads\image4.jpg",
    r"C:\Users\Admin\Downloads\image5.jpg"
]

images = []
for path in image_paths:
    # open, resize, and convert the image to a format
    img = Image.open(path)
    img = img.resize((800, 800))
    images.append(img)

# convert PIL image to ImageTk format for tkinter
final_img = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_img.append(photo)


root.mainloop()