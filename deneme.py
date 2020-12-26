# -*- coding: utf-8 -*-
"""Deneme.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wB3WWWYY0v6ZaBUekC4EtH2TftnlO9tp
"""

!pip install -q sklearn

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x

from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib
from sklearn.model_selection import train_test_split
import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing
from tensorflow.keras import layers
from tensorflow import keras

df=pd.read_csv("/content/ACME-HappinessSurvey2020.csv")

dftrain = df.copy()
dfeval = df.copy()

y_train = dftrain.pop('Y')
y_eval = dfeval.pop('Y')

df.head()

def build_and_compile_model(norm):
  model = keras.Sequential([
      norm,
      layers.Dense(64, activation='relu'),
      layers.Dense(64, activation='relu'),
      layers.Dense(1)
  ])

  model.compile(loss='binary_crossentropy',
                optimizer=tf.keras.optimizers.Adam(0.001),
                metrics=["accuracy"])
  return model

normalizer = preprocessing.Normalization()
normalizer.adapt(np.array(dftrain))

dnn_model = build_and_compile_model(normalizer)
dnn_model.summary()

# Commented out IPython magic to ensure Python compatibility.
# %%time
# history = dnn_model.fit(
#     dftrain, y_train,
#     validation_split=0.2,
#     verbose=0, epochs=100)

test_results = {}
test_results['dnn_model'] = dnn_model.evaluate(dfeval, y_eval, verbose=1)
test_results

