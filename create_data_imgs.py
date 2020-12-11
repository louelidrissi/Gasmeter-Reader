'''

    Program used take pictures to train the analog dial reader code.

'''

import os
import cv2
import time
from datetime import datetime

def close(cam):
    print("Exit key pressed, closing...")
    cam.release()
    cv2.destroyAllWindows()
    exit()

def time_elapsed(cam_num):
    print("Press s to start and c to stop the time needed for one tick")
    start_time = 0
    elapsed_time = 0

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("frame")

    while(True):
        ret, frame = cam.read()

        if ret:
            cv2.imshow("frame", frame)
            k = cv2.waitKey(1)

            if k == ord('s'):
                print("start")
                start_time = time.time()

            if k == ord('c'):
                print("stop")
                elapsed_time = time.time() - start_time

                cam.release()
                cv2.destroyAllWindows()

                print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) )
                break

        else:
            print("Failed to grab frame. Please try again.")
            exit()

    #print("%02d:%02d:%02d" % (elapsed_time // 3600, (elapsed_time % 3600 // 60), (elapsed_time % 60 // 1)))
    return elapsed_time

def start(cam, total_imgs, elapsed_time):
    print("Operation in progress ...")
    img_counter = 0

    while img_counter <= total_imgs:
        img_counter += 1
        ret, frame = cam.read()

        if ret:
            cv2.imshow("frame", frame)
            k = cv2.waitKey(1)

            if k == ord('c'):
                close(cam)

            img_name= "Gasmeter_fullshot"+ str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))+".png"
            #read = cv2.imwrite(os.path.join(path, img_name), frame)
            cv2.imwrite(os.path.join(path, img_name), frame)
            #print("read", read, img_counter ) 
            time.sleep(elapsed_time)

        else:
            print("Failed to grab frame. Please try again.")
            exit()

    close(cam)


def capture(path, cam_num, total_imgs, elapsed_time):
    print("Enter 's' to start taking pictures and 'c' to quit the program at any moment.")

    cam = cv2.VideoCapture(cam_num)
    cv2.namedWindow("frame")

    while(True):
        ret, frame = cam.read()

        if ret:
            cv2.imshow("frame", frame)
            k = cv2.waitKey(1)

            if k == ord('c'):
                 close(cam)

            elif k == ord('s'):
                start(cam, total_imgs, elapsed_time)

        else:
            print("Failed to grab frame. Please try again.")
            exit()

    close(cam)


if __name__ == "__main__":
    print("Please enter the following info:")

    #to fill once project is complete

    print("Enter the camera number (0 or -1)") #look up for what cam num is called
    cam_num = 0 # = input()

    print("Enter the number of pictures you want the program to take")
    total_imgs = 500 # = input()

    print("Indicate the folder you want your images to be saved in: ")
    path = '/Users/labuser/Documents/Dial code/images/'

    elapsed_time = time_elapsed(cam_num)

    capture(path, cam_num, total_imgs, elapsed_time)

    print("The image capture process is over.")
