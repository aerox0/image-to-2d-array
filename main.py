import numpy as np
import pathlib
import json
from PIL import Image

img = Image.open('test.jpg').convert('L')
arr = np.array(img.getdata(), dtype=np.uint8)
arr = np.round(arr / 255)
arr = np.reshape(arr, (93, 63))

file = pathlib.Path('img_arr.json')
file.write_text(json.dumps(arr.tolist()))
