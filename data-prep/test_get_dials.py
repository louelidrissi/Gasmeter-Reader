import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFilter
import csv

def merge_dial_needle(background, foreground):
    fg_w, fg_h = foreground.size
    bg_w, bg_h = background.size
    # in center of the background (dial)
    offset = ((bg_w - fg_w) // 2, (bg_h - fg_h) // 2)
    needleImage.convert('RGBA')
    Image.Image.paste(background, foreground, offset, foreground)
    return background

def generate_data(sample=50000):
    return

def get_label(angle):
    # how are the angle and value of the dial related

    # label & store it in Dictionary
    label[img] = label
    return

def make_square(im, min_size=10, fill_color=(255, 255, 255, 0)):
    x, y = im.size
    #print(x,y)
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im



def generate_data_with_label(label, start_angle, end_angle ):
    count = 0
    current_val = label

    for angle in range(start_angle, end_angle+1):

        # get needle at angle in specific range
        foreground = needleImage.rotate(angle) #rotateImage(needleImage, angle)
        background = dialImage.copy()

        # creates new image
        generated_img = merge_dial_needle(background, foreground)

        output_path= os.path.join('/Users/labuser/Downloads/Honors/DeepGauge-ML-Demo/CustomEstimator/data/category_folders/', str(round(current_val, 2)))
        filename ='Gasmeter_dial_1_{}.bmp'.format(count)

        #save new image in dial_1_imgs folder
        generated_img.save(os.path.join(output_path, filename))

        count = count+1


if __name__ == '__main__':
    imgs_path = '/Users/labuser/Downloads/Honors/Data_Prep' #'/Users/labuser/DeepGauge-ML-Demo/CustomEstimator/data/new_dials'#'/Users/labuser/Documents/Gasmeter-Reader/images/dial_1_imgs/
    needle_img = 'needle2.png'
    dial_img = 'background.png'

    needle = os.path.join(imgs_path, needle_img)
    dial = os.path.join(imgs_path, dial_img)

    needle = Image.open(needle)
    needleImage = make_square(needle, 50, (255, 255, 255, 0))
    #needleImage.show()
    #foreground = needleImage.rotate(angle) #rotateImage(needleImage, angle)

    dial =Image.open(dial)
    dialImage  = make_square(dial, 50, (255, 255, 255, 0))
    #dialImage.show()
    background = dialImage.copy()

    labels = [0.05,
                0.1,
                0.15,
                0.2,
                0.25,
                0.3,
                0.35,
                0.4,
                0.45,
                0.5]

    angle_intervals = [(0,36),
                        (37, 72),
                        (73, 108),
                        (109, 144),
                        (145, 180),
                        (181, 216),
                        (217, 252),
                        (253, 288),
                        (289, 324),
                        (325, 360)]

    interval={}
    c=0

    for label in labels:

        interval[label]=angle_intervals[c]
        angle_interval = interval[label]
        start_angle, end_angle = angle_interval

        generate_data_with_label(label, start_angle, end_angle)

        c=c+1

#print("interval", interval)
