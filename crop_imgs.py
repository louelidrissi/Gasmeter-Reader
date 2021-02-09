
'''
    gets 4 coordinates of area around right dial
'''
import cv2
import csv
import os
import numpy as np
#import label as l

refPt = []
cropping = False

dial_1_filenames = []

def get_imgs(image_files):
    #images=[]
    #input_folder = '/Users/labuser/Documents/Dial code/images/' #run12-24/check_folder_output'
    #for file in image_files: #os.listdir(input_folder):
        #if file == '.DS_Store':
        #    continue
        #else:
    #    images.append(file)

    image_files.sort()
    #sorts in reverse so from big to small
    image_files= sorted(image_files, reverse=True)
    imgs = image_files[:4000]
    imgs.sort()
    return imgs

def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False

        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

    #Run for first train imgs folder
#input_folder = '/Users/labuser/Documents/Dial code/images/run12-24/checked_folder' #'/Users/labuser/Documents/Gasmeter-Reader/images/imgs_12-11/'
#output_folder = '/Users/labuser/Documents/Dial code/images/run12-24/check_folder_output'#'/Users/labuser/Documents/Gasmeter-Reader/images/dial_1_imgs/

    #Run for test folder
print("Enter directory to the dataset and where the cropped images should be stored at.")
input_folder = '/Users/labuser/Documents/Dial code/images/' #'/Users/labuser/Documents/Gasmeter-Reader/images/imgs_12-11/'
output_folder = '/Users/labuser/Documents/Dial code/images/dataset'#'/Users/labuser/Documents/Gasmeter-Reader/images/dial_1_imgs/

image_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.png')]
image_files = get_imgs(image_files)
#print("image_files" , image_files)
image_file = image_files[0]

image = cv2.imread(image_file)

if image is None:
    print("try a new image")
    exit()

clone = image.copy()

#draw_grid
height, width = image.shape[:2]
print("height, width   :", height, width)
x = 0
y = 0

while x < width:
    x += int(width / 16)
    y += int(height / 16)
    cv2.line(image, (x, 0), (x, height), (0, 0, 255), 1)
    cv2.line(image, (0, y), (width, y), (0, 0, 255), 1)

# height, width = image.shape[:2]
# image = cv2.resize(image, (813, 459))

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
print("Now,")
print("Enter 'r' to reset the cropping region")
print("Enter 'c' tobreak from the loopn")
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()

    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break

cv2.destroyWindow("image")

# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    #cv2.imshow("ROI", roi)

#    print("refPt[0][1]", refPt[0][1])
#    print("refPt[1][1]", refPt[1][1])
#    print("refPt[0][0]", refPt[0][0])
#    print("refPt[1][0]", refPt[1][0])

    cv2.waitKey(0)

# close all open windows
cv2.destroyAllWindows()
#img1 = roi

image_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.png')]
image_files = get_imgs(image_files)


print("first image", image_files[0])
image = cv2.imread(image_file)
if image is None:
    print("error encountered with the input image")
    exit()
cv2.imshow("image", image)
key = cv2.waitKey(1)
cv2.destroyWindow("image")


current_val = input("Enter the value of the right dial. We will label the rest of images from the database with imcrements of .05")
#current_val = 0.25
images_paths
dataset = {}
i = 1
for image_file in image_files:
    image = cv2.imread(image_file)
    if i == 3:
        exit()

    if image is None:
        print("error encountered with the input image")
        exit()

    clone = image.copy()
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    output_filename =  "Gasmeter_dial1_{}.png".format(i)
    dial_1_filenames.append(output_filename)
    #print("output_filename", output_filename)
    #output_filename = "cropped_img.jpg"
    image_file
    #saved = cv2.imwrite(os.path.join(output_folder, output_filename), roi)
    saved = cv2.imwrite(os.path.join(output_folder, image_file), roi)
    print("image status    : ", saved)

    #  Find label of current image
    if (current_val >= 0.48):
        current_val = 0.5
        #dataset[output_filename] = current_val
    dataset[output_filename] = current_val
    current_val = current_val + 0.05
        #images.append(filename)
        #values_dial_1.append(current_val)
    # increment variables
    i = i+1

dial_1_filenames.sort()

with open('excel_sheet.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['filename','label'])
    for key, value in dataset.items():
       writer.writerow([key, value])

print("dataset", dataset)

#l.label_dial_1(output_folder)
#crop(image_files)

#split dial_1_imgs into dial_1_imgs_train & dial_1_imgs_test

#sklearn.model_selection.train_test_split(*arrays, **options)

#input_folder = '/Users/labuser/Documents/Gasmeter-Reader/images/dial_1_imgs'
#output_folder = '/Users/labuser/Documents/Gasmeter-Reader/images/dial_1_imgs_train/'

#split_folders.ratio('input_folder', output="output_folder", seed=42, ratio=(.75, .25)) # ratio of split are in order of train/val/test. You can change to whatever you want. For train/val sets only, you could do .75, .25 for example.
#    with open('dataset.csv', 'wb') as csvfile:
#        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#        filewriter.writerow([image_file, current_val])
