import os
import numpy as np
from PIL import Image as img

import time

# Image Size
size_h = 1000
size_w = 1000

# Image Count
img_max = 1000
ctt = 0


while True:
    image_array = np.random.randint(0, 256, size=(size_h, size_w, 3), dtype=np.uint8)

    # Create a PIL Image object from the NumPy array
    image = img.fromarray(image_array, 'RGB')

    # Save the image to a file
    if os.path.exists("imgs/output_image.jpg"):
        old_img = img.open("imgs/output_image.jpg")

        ctt += 1
        if ctt > img_max:
            ctt = 1
        print(ctt)
        old_img.save(f"imgs/old/output_image_{ctt}.jpg")

    image.save("imgs/output_image.jpg")

    time.sleep(0.5)
