from PIL import Image
import tifffile
import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 8):
    if i == 6:
        continue
    file_path = f"landsat-data-1/LE07_L2SP_121011_20220328_20220422_02_T1_SR_B{i}.TIF"
    save_path = f"landsat-7-data/band-{i}.png"
    
    print(file_path)

    img = tifffile.imread(file_path)
    img = Image.fromarray(img)
    img = img.crop((5500, 3000, 7500, 5000))
    img.save(save_path)
