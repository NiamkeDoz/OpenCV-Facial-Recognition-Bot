import os
import numpy as np
from PIL import Image

BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIRECTORY, "images")

y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("jpg") or file.endswith("png"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            print(label, path)
            pil_image = Image.open(path).convert("L") #turns image into grayscale
            image_array = np.array(pil_image, "uint8")
            print(image_array)
