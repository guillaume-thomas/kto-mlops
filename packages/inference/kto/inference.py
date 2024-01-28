from io import BytesIO

import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array


# load and prepare the image
def load_image(filename: str|BytesIO):
    # load the image
    img = load_img(filename, target_size=(224, 224))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img


class Inference:
    def __init__(self, model_path: str):
        self.model = load_model(model_path)

    def execute(self, filepath:str|BytesIO):
        img = load_image(filepath)
        result = self.model.predict(img)
        values = [float(result[0][0]), float(result[0][1]), float(result[0][2])]
        switcher = ['Cat', 'Dog', 'Other']
        prediction = np.argmax(result[0])
        return {"prediction": switcher[prediction], "values": values}
