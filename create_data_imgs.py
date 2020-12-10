'''

Program used take picture to track gas consumption of a gasmeter.
Takes a picture every 1 second.

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

def start(cam, elapsed_time):
    img_counter = 0
    print("Operation in progress ...")
    while img_counter <= 300:
        img_counter += 1
        ret, frame = cam.read()

        if ret:
            cv2.imshow("frame", frame)
            k = cv2.waitKey(1) #& 0xFF

            if k == ord('c'):
                close(cam)

            img_name= "Gasmeter_fullshot"+ str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))+".png"
            #img_name = "opencv_frame_{}.bmp".format(img_counter)
            read = cv2.imwrite(os.path.join(path, img_name), frame)
            print("read", read, img_counter )
            time.sleep(elapsed_time)

        else:
            print("failed to grab frame")
            exit()

    close(cam)



def capture(path, cam_num, imgs_count, elapsed_time):
    cam = cv2.VideoCapture(cam_num)

    cv2.namedWindow("frame")

    print("Press s when you are ready to start taking pictures")

    while(True):
        ret, frame = cam.read()
        if ret:
            cv2.imshow("frame", frame)
            k = cv2.waitKey(1) #& 0xFF
            #cam.release()
            if k == ord('c'):
                 close(cam)

            elif k == ord('s'):
                start(cam, elapsed_time)

        else:
            print("failed to grab frame")
            exit()
    close(cam)


def time_elapsed(cam_num):
    start_time = 0
    elapsed_time = 0

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("frame")

    print("Press s to start and c to stop the time needed for one tick")


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
            print("failed to grab frame")
            exit()

    #print("%02d:%02d:%02d" % (elapsed_time // 3600, (elapsed_time % 3600 // 60), (elapsed_time % 60 // 1)))

    return elapsed_time



if __name__ == "__main__":
    print("Enter 's' to start taking pictures and 'c' to quit the program at any moment.")
    print("Pls enter the camera number (0 or -1)")
    cam_num = 0 # = input()

    elapsed_time = time_elapsed(cam_num)

    print("Pls enter the number of pictures you want the program to take")
    imgs_count = 500 # = input()

    path= '/Users/labuser/Documents/Dial code/images/'

    capture(path, cam_num, imgs_count, elapsed_time)
    print("capture over")
