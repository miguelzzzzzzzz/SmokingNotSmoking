import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tkinter as tk
from tkinter import ttk  # for themed widgets
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

# Suppress TensorFlow warnings
tf.get_logger().setLevel('ERROR')
import tensorflow_hub as hub


class SmokingDetector:
    def __init__(self, master=None):
        # Create the main frame
        frame1 = ttk.Frame(master, height=700, width=600)

        # Set the background gradient (similar to the image)
        gradient_frame = tk.Canvas(frame1, width=600, height=700)
        gradient_frame.place(x=0, y=0)

        color1 = "#F1D1B5"  # Light pink from the image
        color2 = "#568EA6"  # Light blue from the image

        gradient_frame.create_rectangle(0, 0, 600, 700, fill=color2, width=0)
        for i in range(700):
            ratio = i / (700 - 1)
            color_value1 = int(color1[1:3], 16)  # Convert hex string to integer (R, G, B)
            color_value2 = int(color2[1:3], 16)
            color_value = int(
                color_value1 * ratio + color_value2 * (1 - ratio))  # Interpolate integer values
            color = "#" + ("%02x" % color_value) * 3  # Repeat color value for RGB

            gradient_frame.create_rectangle(0, i, 600, i + 1, fill=color, width=0)

        # Title label with a more modern font
        title_label = ttk.Label(frame1, font=("Arial", 25, "bold"),
                                text='Smoking and Not Smoking Detector')
        title_label.place(anchor="center", relx=0.5, rely=0.1, x=0, y=0)

        # Image label with a raised border
        self.image_label = ttk.Label(frame1, relief="raised")
        self.image_label.place(anchor="center", relx=0.5, rely=0.39, x=0, y=0)

        # Select image button with a flat style
        select_button = ttk.Button(frame1, style='Kim.TButton', text='Select Image',
                                   command=self.select_image)
        select_button.place(anchor="center", height=50, relx=0.5, rely=0.65, width=200, x=0, y=0)

        # Check button with a raised style
        check_button = ttk.Button(frame1, style='Kim.TButton', text='SCAN',
                                  command=self.predict_image)
        check_button.place(anchor="center", height=50, relx=0.5, rely=0.75, width=200, x=0, y=0)

        # Result label with a clear font
        self.result_label = ttk.Label(frame1, font=("Arial", 24, "bold"),
                                     text='Waiting for image...')
        self.result_label.place(anchor="center", relx=0.5, rely=0.85, x=0, y=0)

        frame1.pack(anchor="center", expand=True, side="top")

        self.mainwindow = frame1

        # Load the pre-trained model
        self.model = hub.load('./newmodel/newmodel')

    def run(self):
        self.mainwindow.mainloop()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ("All files", "*.*")))
        if file_path:
            self.image = Image.open(file_path).resize((300, 300))
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.configure(image=self.photo)
            self.image_label.image = self.photo

    def predict_image(self):
        if all(hasattr(self, attr) for attr in ('model', 'photo', 'image')):
            image = np.array(self.image.convert("RGB").resize((250, 250)), dtype=np.float32) / 255.0
            image = np.expand_dims(image, axis=0)

            prediction = self.model(image)
            class_index = np.argmax(prediction[0])
            result = 'Not Smoking' if class_index == 0 else 'Smoking'

            self.result_label.configure(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x700")
    root.title("Smoking Detector")
    app = SmokingDetector(root)
    app.run()