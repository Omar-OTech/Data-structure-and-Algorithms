import tkinter as tk
import math

# Initialize the window
root = tk.Tk()
root.title("Circle Pattern")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Function to draw the circles
def draw_circles():
    w, h = 300, 300  # Center point
    r = 200  # Radius
    for i in range(12):
        angle = (i * 360 / 12) * math.pi / 180  # Convert degrees to radians
        x = w + r * math.cos(angle)
        y = h + r * math.sin(angle)
        canvas.create_oval(x-25, y-25, x+25, y+25, outline="black", width=2)

# Call the function to draw the circles
draw_circles()

# Start the GUI event loop
root.mainloop()
