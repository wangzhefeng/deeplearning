import numpy as np
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.models import Model


"""
Extract features from an arbitrary intermediate layer with VGG19
"""


base_model = VGG19(weights = 'imagenet')
model = Model(inputs = base_model.input, outputs = base_model.get_layer('block4_pool').output)
img_path = 'elephant.jpg'
img = image.load_img(img_path, target_size = (224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)
x = preprocess_input(x)
block4_pool_features = model.predict(x)
