import numpy as np
from keras.models import load_model
from cv2 import imread,resize,IMREAD_GRAYSCALE,INTER_AREA
from res_im import *


def func():
    model_load = load_model('lenet.h5')
    resize_image(input_image_path='photo.png',
                 output_image_path='caterpillar_small.png',
                 size=(28, 28))
    img = imread('caterpillar_small.png', IMREAD_GRAYSCALE)
    output = img.copy()
    img = img.reshape(-1, 28, 28, 1)
    img = img.astype('float32')
    y_pred =model_load.predict_classes(img)
    print(y_pred)


