import PIL
from PIL import Image
import os

for image in os.listdir(os.getcwd()):
    
    im = Image.open(image)

    out = im.transpose(PIL.Image.FLIP_LEFT_RIGHT) 
    out.save(image)
