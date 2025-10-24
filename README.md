# Gasmeter Digit and Dial Reading using Image Classification


# Table of Contents

1. [Set-up](#set-up)
2. [Data Pre-Processing](#data-pre-processing)
3. [Classification Guidelines](#classification-guidelines)
4. [Training Input Sample](#training-input-sample)
5. [Testing Input Sample](#testing-input-sample)
6. [CNN Model Architecture](#cnn-model-architecture)
7. [Confusion matrix for Dial-Reader](#confusion-matrix-for-dial-reader)
8. [Confusion matrix for Digit-Reader](#confusion-matrix-for-digit-reader)
9. [Model Reference](#model-based-on-deepgauge-ml-demo-github)
10. [Future Improvements](#future-improvements)

## Set-up:
A simple USB Camera is set up in front of the Gasmeter to collect images. A Stepper Motor Controller is used to run the Gasmeter and control image capture rate and labeling. The Gasmeter and camera are assumed to be fixed in place during the reading process.

<img src="https://github.com/user-attachments/assets/9136662c-9cc6-4ca6-824d-9c6b7a6ec2f8" alt="stepperMotorController" width="300" />


## Classification Guidelines: 
To create labeled Dial dataset for supervized image classification, the dial is divided into 9 sections (0-9). Each section indicates different needle positions. So the reading is approximated to +/- 0.05 as show by the table below. Each digit is assigned to a corresponding category, 0 to category 0, 1 to category 1 and so on. 

<img src="https://github.com/user-attachments/assets/90b39faa-7640-4459-b17d-2753831c4f7a" alt="label_cat" height="400" />

## Data Pre-Processing:
Gasmeter's digits and dials are selected by the user as shown below. Using OpenCV, the coordinates of the selected section are then saved and used for all captured images.

<img src="https://github.com/user-attachments/assets/076b27ff-a851-4bc2-a034-89f20a3550a7" alt="gasmeter_red" width="300" />

Due to time constraints, the needle detection process was left out for the initial phase of this project. Photoshop was used to separate the needle in the upfront position from the dial, generating multiple images of needles and dials to train and test the model on variations. The needle images were then merged with dial images and rotated across categories and labeled accordingly using Python Imaging Library.

Data was augmented to account for light and gasmeter screen effect on the needle's images, and potential scratched. Training and testing dataset include unique images with no overlap between the datasets. 

## Training Input Sample:

<img src="https://github.com/user-attachments/assets/4358cdd1-fa8d-47c0-ae86-c043b944212f" alt="generated_dataset_example" width="500" />
<img src="https://github.com/user-attachments/assets/42bce19a-ad26-42b0-9777-2a3df5064731" alt="temp_TRAIN" width="500" />

## Testing Input Sample:

<img src="https://github.com/user-attachments/assets/1d2721a7-cc2c-4214-bf16-213a9691618b" alt="temp" width="500" />
<img src="https://github.com/user-attachments/assets/c0533a46-27d3-49ad-b793-bdf152030422" alt="temp_vali" width="500" />

## CNN Model Architecture:

<img src="https://github.com/user-attachments/assets/692a1a74-d239-4a5c-bd3b-bfc6ad445a45" alt="archi2" width="500" />

## Confusiong matrix for Dial-Reader: 

<img src="https://github.com/user-attachments/assets/bdf81473-adea-4b8b-9729-46b25b32482a" alt="confusinmactix" width="500" />

## Confusiong matrix for Digit-Reader:

<img src="https://github.com/user-attachments/assets/ef3a55a5-1066-48e3-ba2d-dfd5b471cdfa" alt="cm with digit lables" width="500" />


## Model Referense Repository: 

Model used in the implementation of the Dial and Digit Reader is based on part of the Gauge Reaser Deep Learning Model in the following repository: [DeepGauge-ML-Demo GitHub](https://github.com/louelidrissi/DeepGauge-ML-Demo)

## Future Improvements:
- Implement image recognition to detect the needle.
- Connect CNN model to a front-end interface with Cloud database.
