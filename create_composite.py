from argparse import ArgumentParser
from PIL import Image
import tifffile
import numpy as np
import matplotlib.pyplot as plt



parser = ArgumentParser()
parser.add_argument("--band_1", type=str, required=True)
parser.add_argument("--band_2", type=str, required=True)
parser.add_argument("--band_3", type=str, required=True)

args = parser.parse_args()

crop_info = (5500, 3000, 7500, 5000)

band_1 = tifffile.imread(args.band_1)
band_1 = Image.fromarray(band_1)
band_1 = band_1.crop(crop_info)
band_1 = np.array(band_1)


band_2 = tifffile.imread(args.band_2)
band_2 = Image.fromarray(band_2)
band_2 = band_2.crop(crop_info)
band_2 = np.array(band_2)


band_3 = tifffile.imread(args.band_3)
band_3 = Image.fromarray(band_3)
band_3 = band_3.crop(crop_info)
band_3 = np.array(band_3)

img = np.stack([band_1, band_2, band_3]).T
img = ((img / img.max()) * 255).astype('uint8')
img = Image.fromarray(img)
print(img)

plt.imshow(img)
plt.show()
plt.imsave("composite-2.png", img)