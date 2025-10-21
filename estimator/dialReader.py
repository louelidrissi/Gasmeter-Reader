import matplotlib.pyplot as plt
import numpy as np
from modules.primary_models_modules.train_modules import LoadImg
from modules.primary_models_modules.train_modules import OptimizeAndLog
from modules.ensemble_modules.trainer_from_storage.trainer import model
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
#warnings.filterwarnings("ignore")


def train_model_dial_imgs():
    #   datasets can be obtained via LoadImg module.
    X_train, X_validation, y_train, y_validation, cls_indices = LoadImg.Dataset.prep_datasets(
        ver_ratio=0.2, container_path='/Users/labuser/Downloads/Honors/DeepGauge-ML-Demo/CustomEstimator/data/DigitsTrainingImgs',
        final_img_width=79, final_img_height=79,
        color_mode="grayscale", random_state=1911)

    print('There are {} images in the train dataset.'.format(X_train.shape[0]))
    print('There are {} images in the validation dataset.'.format(X_validation.shape[0]))
    print('The images shape is {}'.format(X_train.shape[1:]))


        #   Training Data Samples
    fig = plt.figure(figsize=(15,2.5))
    imgs_num = np.random.choice(range(len(X_train)), 6)

    for i, img_num in enumerate(imgs_num):
        ax = fig.add_subplot(1, 6, i + 1, xticks=[], yticks=[])
        ax.imshow(X_train[img_num, :, :, 0], cmap='gray')
        ax.set_title('category {}_train'.format(np.argmax(y_train[img_num])))


    fig.savefig('temp_train.png', dpi=fig.dpi)

        #   Validation Data Samples

    fig = plt.figure(figsize=(15,2.5))
    imgs_num = np.random.choice(range(len(X_validation)), 6)

    for i, img_num in enumerate(imgs_num):
        ax = fig.add_subplot(1, 6, i + 1, xticks=[], yticks=[])
        ax.imshow(X_validation[img_num, :, :, 0], cmap='gray')
        ax.set_title('category {}_val'.format(np.argmax(y_validation[img_num])))


    fig.savefig('temp_vali.png', dpi=fig.dpi)

        #      Primary Models Training
    fig = plt.figure(figsize=(15,2.5))
    ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[])
    ax.imshow(X_train[4, :, :, 0], cmap='gray')
    ax.set_title('category {}_train'.format(np.argmax(y_validation[2])))

    fig.savefig('1.png', dpi=fig.dpi)

        #   Validation Data Samples
    fig = plt.figure(figsize=(15,2.5))
    imgs_num = np.random.choice(range(len(X_train_2)), 6)

    for i, img_num in enumerate(imgs_num):
        ax = fig.add_subplot(1, 6, i + 1, xticks=[], yticks=[])
        ax.imshow(X_train_2[img_num, :, :, 0], cmap='gray')
        ax.set_title('category {}_train'.format(np.argmax(y_train_2[img_num])))


    fig.savefig('2.png', dpi=fig.dpi)

    ##
    '''
    OptimizeAndLog.OptimizerLogger. \
        train_and_save_logs_three_CNN(filter_size1=17, num_filters1=45, strides_1=[1, 7, 7, 1],
                                      use_pooling_1=True, pooling_ksize_1=[1, 4, 4, 1], pooling_strides_1=[1, 4, 4, 1],
                                      ##
                                      filter_size2=7, num_filters2=17, strides_2=[1, 5, 5, 1],
                                      use_pooling_2=True, pooling_ksize_2=[1, 3, 3, 1], pooling_strides_2=[1, 3, 3, 1],
                                      ##
                                      filter_size3=1, num_filters3=7, strides_3=[1, 1, 1, 1],
                                      use_pooling_3=False, pooling_ksize_3=None, pooling_strides_3=None,
                                      ##
                                      fc_size=86,
                                      num_iterations=500,
                                      learning_rate=1e-4, momentum=None,
                                      X_train=X_train, y_train=y_train,
                                      X_test=X_validation, y_test=y_validation,
                                      models_log_path='./modules/primary_models_modules/logs/models/',
                                      cls_indices=cls_indices,
                                      keep_best_model = True,
                                      padding='SAME',
                                      device_name="/cpu:0")
                                      '''

def serving_input_receiver_func():
    images_str = tf.placeholder(tf.string, shape=[None], name='export_input_image_bytes')
    def decode_and_resize(image_str_tensor):
        image = tf.image.decode_jpeg(image_str_tensor, channels=3)
        image = tf.expand_dims(image, 0)
        image = tf.image.resize_bilinear(image, [224, 224], align_corners=False)
        image = tf.squeeze(image, squeeze_dims=[0])
        return image
    images = tf.map_fn(decode_and_resize, images_str, dtype=tf.float32)
    return tf.estimator.export.ServingInputReceiver({'img': images}, {'bytes': images_str})

if __name__ == "__main__":
    train_model_dial_imgs()
