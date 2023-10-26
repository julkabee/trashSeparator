import camera
import validation
import serial
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

folder_path = "C:/Users/PC/PycharmProjects/trashSeparator/camera"
model_path = "C:/Users/PC/PycharmProjects/trashSeparator/my_model.keras"
newdataset_path = "C:/Users/PC/PycharmProjects/trashSeparator/newdatasets"

port = "COM5"
arduino = serial.Serial(port, 9600)

camera.makingFrames(folder_path, newdataset_path)
predicted_class = validation.checkImages(model_path, folder_path)
print(predicted_class)
predicted_class = '#' + str(predicted_class) + ';'
predicted_class = bytes(str(predicted_class), 'utf-8')
arduino.write(predicted_class)
camera.exit()
