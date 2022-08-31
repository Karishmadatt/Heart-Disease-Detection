import numpy
from keras.models import load_model
import tensorflow as tf
import pandas as pd
import pickle

# filepath = 'model .pkl'
# object = pd.read_pickle(r'filepath')
model=pickle.load(open('model_joblib_heart.pkl','rb'))

# filepath = '/home/karishma/Desktop/Heart disease prediction/sem vi  project/ANN_model.pb'
# new_model = tf.keras.models.load_model('ANN_model.h5')
# model = tf.keras.models.load_model('saved_model/my_model/xgboost.pb')
# model = tf.keras.models.load_model('xgboost.pkl')
# loaded_model = tf.keras.models.load_model('xg.model')
# Load the model
# tf.lite.TFLiteConverter.from_keras_model(filepath)
# model = load_model(filepath, compile = True)

# A few random samples
use_samples = [[56,1,0,132,184,0,0,105,1,2.1,1,1,1]]
# samples_to_predict = []

# Convert into Numpy array
samples_to_predict = numpy.array(use_samples)

# Generate predictions for samples
predictions = model.predict(samples_to_predict)
print(predictions[0])
if predictions==1:
    print('Heart Disease')
elif predictions==2:
    print('No Heart Disease')