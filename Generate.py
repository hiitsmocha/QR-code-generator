import tkinter 
from PIL import ImageTk, Image
import pyqrcode

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width = 400, height = 400)
white = [255,255,0]
canvas
canvas.pack()
app_label = tkinter.Label(root, text = "QR Code Generator", fg = "white", font = ("Arial", 30))
canvas.create_window(200, 50, window = app_label)
root.mainloop()




