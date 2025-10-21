from sklearn.datasets import load_files
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np
from keras.preprocessing import image
import pandas as pd
import pickle
import json, os
from PIL import Image
from collections import OrderedDict

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

class DatasetForPrediction(object):

    def __init__(self):
        self.category_mapper = dict()
        self.MultiColumnOneHotEncoder = object()

    @staticmethod
    def initialize():
        # Data to be written
        dictionary = {
            "num_to_cat": {"0": "0.05", "1": "0.1", "2": "0.15", "3": "0.2", "4": "0.25", "5": "0.3", "6": "0.35", "7": "0.4", "8": "0.45", "9": "0.5"},
            "cat_to_num": {"0.05": 0, "0.1": 1, "0.15": 2, "0.2": 3, "0.25": 4, "0.3": 5, "0.35": 6, "0.4": 7, "0.45": 8, "0.5": 9},
            "num_classes": 10
        }

        # Serializing json
        json_object = json.dumps(dictionary, indent = 3)
        # Writing to sample.json
        with open("/Users/labuser/Downloads/Honors/DeepGauge-ML-Demo/CustomEstimator/modules/primary_models_modules/dumps/category_mapper.json", "w") as outfile:
            outfile.write(json_object)
        ##
        with open('/Users/labuser/Downloads/Honors/DeepGauge-ML-Demo/CustomEstimator/modules/primary_models_modules/dumps/MultiColProcessor.pkl', 'rb') as handle:
            DatasetForPrediction.MultiColumnOneHotEncoder = pickle.load(handle)
        ##
        with open(os.path.expanduser('/Users/labuser/Downloads/Honors/DeepGauge-ML-Demo/CustomEstimator/modules/primary_models_modules/dumps/category_mapper.json')) as handle:
            DatasetForPrediction.category_mapper = json.load(handle)
        return

    @staticmethod
    def load_dataset(path):
        #data = load_files(path, load_content=False)
        ##
        guage_files_ = np.empty(shape = 0, dtype = gauge_categories_.dtype) #np.array(data['filenames'])
        #gauge_categories_ = np.array(data['target'])

            #   Get ALL files
        image_files = [os.path.join(path, file) for file in os.listdir(path) if file.endswith('.png')]

        #   Images to arrays
        for image_file in image_files:
            img = load_img(image_file)
            img_arr = img_to_array(img, data_format=None, dtype=None)
            guage_files_= np.append(guage_files_, img_arr)

        guage_files  = np.empty(shape = 0, dtype = guage_files_.dtype)
        #gauge_categories= np.empty(shape = 0, dtype = gauge_categories_.dtype)
        print("guage_files_", guage_files_)

            #   Get data imgs file
        for img_path in guage_files_:
            if os.path.basename(img_path) != '.DS_Store':
                index = np.where(guage_files_ == img_path)
                to_append1 = np.array(guage_files_[index])
                #to_append2 = np.array(gauge_categories_[index])
                guage_files = np.append(guage_files,to_append1 )
                #gauge_categories= np.append(gauge_categories, to_append2)

        return guage_files      #, gauge_categories

    @staticmethod
    def path_to_tensor(img_path, img_size_x, img_size_y, color_mode):
        # loads RGB image as PIL.Image.Image type
        img = image.load_img(img_path, target_size=(img_size_y, img_size_x, color_mode))
        # convert the img to 3D tensor with shape (?, ?, ?)
        x = image.img_to_array(img)
        # convert 3D tensor to 4D tensor with shape (1, ?, ?, ?) and return 4D tensor
        return np.expand_dims(x, axis=0)

    @staticmethod
    def paths_to_tensor(imgs_path, img_size_x, img_size_y, color_mode):
        list_of_tensors = [DatasetForPrediction.path_to_tensor(
            img_path, img_size_x, img_size_y, color_mode) for img_path in list(imgs_path)]
        return np.vstack(list_of_tensors)

    @classmethod
    def return_datasets(cls, container_path, final_img_width, final_img_height,
                        color_mode='grayscale'):
        ##
        cls.initialize()
        ##
        guage_files = cls.load_dataset(path=container_path) #, gauge_categories
        print("guage_files", guage_files)
        ##
        X_pred = cls.paths_to_tensor(imgs_path=guage_files, img_size_x=final_img_width,
                                     img_size_y=final_img_height,
                                     color_mode=color_mode)

        ##
        #y_pred_cat = pd.DataFrame(data=gauge_categories, columns=['y_true'], dtype='category')
        #y_pred = cls.MultiColumnOneHotEncoder.transform(data=y_pred_cat)

        ##
        return  X_pred, guage_files #,y_pred.values
