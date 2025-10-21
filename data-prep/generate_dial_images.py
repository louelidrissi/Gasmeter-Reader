import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFilter
import csv
import time
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

#   Gloabl Variables
count = 0
first_val = {}

first_val['horizontal_needle_1.png']= 0.05

# Dictionary that maps label to the angle interval
get_angle_interval = {}

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

angle_interval_end = [36,
                        72,
                        108,
                        144,
                        180,
                        216,
                        252,
                        288,
                        324,
                        361]

angle_interval_start = [0,
                    37,
                    73,
                    109,
                    145,
                    181,
                    217,
                    253,
                    289,
                    325]

start_angle_dic = {}
end_angle_dic = {}

def label_to_angle_interval():
    global labels, angle_interval_start, angle_interval_end, start_angle_dic, end_angle_dic
    c = 0
    # Loop through all labels
    while c != 10:
        # Get lable
        label = labels[c]
        #   Get start and end of rotation for this label
        s = angle_interval_start[c]
        e = angle_interval_end[c]
        # do labeling
        start_angle_dic[label] = s
        end_angle_dic[label] = e
        c = c+1
#    print(start_angle_dic)
    return

next_dic = {}
def create_next_dict():
    global labels, next_dic
    c = 0
    next = 0
    # Loop through all labels
#    print("labels length", len(labels))
    for label in labels:
    #    print("c",c)
    #    print("label", label)
        if label == 0.5:
            next_dic[label]=labels[0]
            break
            #print(" c is 10 next_dic", next_dic)
        if c != 10:
            next_dic[labels[c]] = labels[c+1]
            #print("0<c<10 next_dic", next_dic)
        c = c+1
    return

def merge_dial_needle(background, foreground):
    fg_w, fg_h = foreground.size
    bg_w, bg_h = background.size
    # in center of the background (dial)
    offset = ((bg_w - fg_w) // 2, (bg_h - fg_h) // 2)
    Image.Image.paste(background, foreground, offset, foreground)
    return background

def get_label(label):
    return next_dic[label]

def make_square(im, min_size=10, fill_color=(255, 255, 255, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

def get_filenames():
    imgs_path = '/Users/labuser/Downloads/Honors/Data_Prep/Needlepath/'
    list = []
    for needle_img in os.listdir(imgs_path):
        if needle_img.endswith(".png"):
            list.append(needle_img)
    return imgs_path, list

def generate_all_dataset():
    global first_val, labels

    #   Needle image filename
    needle_img_list = ['Gasmeter_dial_1_456 (1).png',
                            'Gasmeter_dial_1_310 (1).png',
                            'Gasmeter_dial_1_314 (1).png',
                            'Gasmeter_dial_1_391 (1).png',
                            'Gasmeter_dial_1_395 (1).png']

    for needle_img in needle_img_list:
        i = 0
        #   Get the the needle's start reading
        needle_val = 0.05

        # Dial image Filename
        dial_img = 'image.png'

        imgs_path, list = get_filenames()
        total_imgs_count = 0

        #print("all images used to generate dataset: ", first_val.keys())
        #for needle_img in first_val.keys():


        #   Generate training dataset
        #print("needle img name", needle_img)
        #print("needle_val",needle_val)

        count = generate_dataset(needle_val, imgs_path, needle_img, dial_img)
        total_imgs_count  = total_imgs_count + count
        #break
        print("total_imgs_count ", total_imgs_count)
    #print("LIST of needle_img: ",list)


def get_interval(current_val):
    global angle_intervals
    interval = {}
    label = 0.3
    for angle_interval in angle_intervals:
        #print("angle_interval", angle_interval)
        start_angle, end_angle = angle_interval
        #current_val = label
        #print("start_angle", start_angle)
    return start_angle, end_angle# current_val

def generate_dataset(start_val, imgs_path, needle_img, dial_img):
    #print("start_val", start_val)
    global count, labels, angle_intervals
    #   Get node from SingleLinkedList with the value of the needle's reading
    #start_node = labels_linked_list.unordered_search(start_val)


#    print("start_node",start_node)
    #labels_linked_list.output_list(start_val_node)
    #print("start_val_node2",output_list(labels_linked_list))

    #   Open & crop foregound  and background imgs
    dial = os.path.join(imgs_path, dial_img)
    needle = os.path.join(imgs_path, needle_img)

    needle = Image.open(needle)
    dial = Image.open(dial)
    nsize = needle.size
    dsize = dial.size
    print("nsize", nsize)
    print("dsize", dsize)

    dialImage  = make_square(dial, 50, (255, 255, 255, 0))
    needleImage = make_square(needle, 50, (255, 255, 255, 0))

    background = dialImage.copy()

    # Call with label to get start and end of angle
    #start_angle = start_angle_dic[current_label]
    #end_angle = end_angle_dic[current_label]
    #   Get the to be created imgs label & angle interval of the needle in that region
    #while i != 10:#val_node.next.has_value(start_val_node.data):
    #    current_label = val_node.data
    c = 0
    count = 0
    current_label = start_val
    while c != 11:
        print("current_label", current_label )
        start_angle = start_angle_dic[current_label ]
        end_angle = end_angle_dic[current_label ]
        #   print("current_label (be 3)", current_label)

        for angle in range(start_angle, end_angle):

            # Get needle at angle in specific range
            foreground = needleImage.rotate(angle) #rotateImage(needleImage, angle)
            needleImage.convert('RGBA')
            background = dialImage.copy()
            # Creates new image & Save new image in specific folder
            generated_img = merge_dial_needle(background, foreground)
            output_path = os.path.join('/Users/labuser/Downloads/Honors/Data_Prep/quad1', str(round(current_label, 2)))
            # /Users/labuser/Downloads/Honors/DeepGauge-ML-Demo/CustomEstimator/data/testFolder
            filename ='Gasmeter_dial_1_{}_{}_{}.bmp'.format(count, needle_img, dial_img)
            print("filename", filename)
            generated_img.save(os.path.join(output_path, filename))

            count = count+1

        current_label = next_dic[current_label]
        c = c+1


    #i = i+1
    return count

if __name__ == '__main__':
    # create label_to_cat()
    label_to_angle_interval()
    create_next_dict()
    print("next_dic", next_dic)
    #print("end_angle_dic",end_angle_dic)

    generate_all_dataset()
