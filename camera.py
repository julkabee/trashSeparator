import cv2
import os
import time

camera = cv2.VideoCapture(0)


def countFiles(folder_path):
    files = os.listdir(folder_path)
    count = 0
    for file in files:
        if os.path.isfile(os.path.join(folder_path, file)):
            count += 1
    return count


def deleteFiles(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


def exit():
    camera.release()
    cv2.destroyAllWindows()


def makingFrames(folder_path, newdataset_path):
    i = 0
    count = countFiles(newdataset_path)
    deleteFiles(folder_path)
    ret, frame = camera.read()
    cv2.imshow("Camera", frame)
    time.sleep(3)
    cv2.imwrite(os.path.join(folder_path, "frame" + str(i) + ".jpg"), frame)
    cv2.imwrite(os.path.join(newdataset_path, "frame" + str(count + 1) + ".jpg"), frame)











