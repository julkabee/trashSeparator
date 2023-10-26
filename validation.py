import os
import keras


def checkImages(model_path, folder_path):
    model = keras.models.load_model(model_path)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        img = keras.preprocessing.image.load_img(file_path, target_size=(224,224))
        img = keras.preprocessing.image.img_to_array(img)
        img = img.reshape((1,) + img.shape)
        img /= 255.0

        result = model.predict(img)
        predicted_class = result.argmax()

        return predicted_class


