
from argparse import ArgumentParser
from PIL import Image

import matplotlib.pyplot as plt
import os
import tifffile
import numpy as np

# TIFF_DIRECTORY = "three_band"
# PNG_DIRECTORY = "urban_outputs"

# os.makedirs(PNG_DIRECTORY, exist_ok=True)

# files = os.listdir(TIFF_DIRECTORY)
# for (i, file_name) in enumerate(files):
#     print(f"\r{i}/{len(files)}", end="")
#     img = tifffile.imread(f"{TIFF_DIRECTORY}/{file_name}").transpose(1, 2, 0)
#     img = img / img.max()
#     plt.imsave(f"{PNG_DIRECTORY}/{file_name[:-3]+'.png'}", img)
#     # img.save(f"{PNG_DIRECTORY}/{file_name[:-3]+'.png'}")

# print()


parser = ArgumentParser()
parser.add_argument("--file_path", type=str, required=True)


args = parser.parse_args()
img = tifffile.imread(args.file_path)
img = Image.fromarray(img)

img = img.crop((5500, 3000, 7500, 5000))

plt.imshow(img, 'gray')
plt.show()
