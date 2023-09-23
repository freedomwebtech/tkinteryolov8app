import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
from tkinter import filedialog

root=tk.Tk()
your_name_label = tk.Label(root,font="Calibri, 20", text="Yolo V8 Object Detection")
your_name_label.pack()

root.mainloop()
