import tensorflow as tf
from keras.models import load_model

# Load the model (if it was previously saved in a different format, e.g., .h5)
model = load_model('Bitcoin_Price_prediction_Model.keras')


print(tf.__version__)
