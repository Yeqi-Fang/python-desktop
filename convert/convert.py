import pydicom
import os
import glob
from PIL import Image
import numpy as np



os.chdir(r'E:\Data\new')
for path in glob.glob('*.dcm'):
    name = path.split('.')[0]
    im = pydicom.dcmread(path)
    im = im.pixel_array.astype(float)
    rescaled_image = (np.maximum(im,0)/im.max())*255 # float pixels
    final_image = np.uint8(rescaled_image) # integers pixels
    final_image = Image.fromarray(final_image)
    final_image.save(f'png/{name}.png')
