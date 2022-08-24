from email.mime import image
from PIL import Image
from io import BytesIO
from serve.serve_model import *
import cv2

path = "/home/kiet/Documents/Ocr-fork/Ocr-cccd/samples/1.png"

im = cv2.imread(path)

prediction = predict(im)
print(prediction)


