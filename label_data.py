'''
        Labels the training dataset pictures
      &
        Saves them to a csv file
        
        dial1 is the 0.5 cf dial
        dial2 is the 2cf dial

'''
import os
import cv2
import time
from datetime import datetime
from PIL import Image
import csv
import cv2 as cv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def label_dial1(path1):

    '''
        The first picture in the loop should have the needle at 12 o'clock
    '''

    dataset = {}
    val_dial_1 = 0

    for filename in os.listdir(path1):
 
        if (val_dial_1 >= 0.5):
        
            #print("max reached")
            #print("current val_dial_1", val_dial_1)
            val_dial_1 = 0
            #print("rewind val_dial_1", val_dial_1)
            dataset[filename] = val_dial_1

        if (val_dial_1 < 0.5):
        
            val_dial_1 = val_dial_1 + 0.05
            #print("tracking val_dial_1", val_dial_1)
            dataset[filename] = val_dial_1

        else:
            print("incorrect val_dial_1 encountered", val_dial_1)
            break

    #print("filenames", filenames)
    #print("values_dial_1", values_dial_1)

 
    label = pd.DataFrame(list(dataset.items()),columns = ['filename', 'label_dial_1'])
    #print(label)
    label.to_csv('label_1.csv', index=False)

'''
def label_dial2(path2):
    vals_dial2 = []
    val_dial2 = 0

    for filename in os.listdir(path2):

        if (val_dial2 == 2):
            val_dial2 = 0

        val_dial2 = val_dial2 + 0.2
        print("label", val_dial2)

    label = {'vals_dial2': vals_dial2}
    label = pd.DataFrame(label)
    label.to_csv('label2.csv', index=False)
'''

if __name__ == "__main__":
    #path1 = '/Users/labuser/Documents/Dial code/images/'
    #path2 =
    path1 = '/Users/labuser/Documents/label_imgs/'

    label_dial1(path1)
    #label_dial2(path2)
