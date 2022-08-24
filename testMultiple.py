from email.mime import image
from PIL import Image
from io import BytesIO
from serve.serve_model import *
import cv2
import matplotlib.pyplot as plt
import os 

path = "/home/kiet/Documents/Ocr-fork/Ocr-cccd/samples"
files = os.listdir(path)
files.sort()
#Show anh matplotlib

height = 3
width = 3

f, axarr = plt.subplots(height, width) 
f.set_figheight(height * 5)
f.set_figwidth(width * 5)

for i in range (9):
    image_file = os.path.join(path, str(files[i]))
    
    im = cv2.imread(image_file)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB )
    
    axarr[int(i/3)][int(i%3)].imshow(im)
    
    print(files[i])
    prediction = predict(im)
    print(prediction)

plt.show()

