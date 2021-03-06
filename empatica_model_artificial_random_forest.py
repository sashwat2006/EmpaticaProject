# -*- coding: utf-8 -*-
"""Empatica Model Artificial RANDOM FOREST

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wIOnxgiorYczhT8LxxQiUVf79wDTsMwY
"""

# Run the code cell.
import firebase_admin
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets

import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
path = "https://raw.githubusercontent.com/sashwat2006/EmpaticaProject/main/ArtificialDatasetEmpatica.csv"
data = pd.read_csv(path)
data.head()

data.info()

from sklearn.model_selection import train_test_split

features = data[["TEMP","HR","EDA"]]
target = data["FINAL FLAG"]

x_train,x_test,y_train,y_test = train_test_split(features,target,test_size=0.3,random_state=42)

x_train.shape

y_train.shape

from sklearn.ensemble import RandomForestClassifier

RF_model = RandomForestClassifier(n_estimators=100,n_jobs=-1)
RF_model.fit(x_train,y_train)

score = RF_model.score(x_train,y_train)
score

prediction = RF_model.predict(x_test)

# TESTING WITH JUST ONE ROW
#arr = x_test.iloc[0,:]
#arr = arr.values.reshape(1,3)
#print(arr)
#prediction = RF_model.predict(arr)
#prediction

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,prediction))
print(confusion_matrix(y_test,prediction))

# XG Boost, RF, SVC, Logistic Reg

"""
In this case,
 - positive outcome $\Rightarrow$ class `1` (patients with unhealthy heart rate)
 - negative outcome $\Rightarrow$ class `0` (patients with healthy heart rate)

The confusion matrix reflects the following values:

1. **True Negatives (TN)** - class `0` values **correctly** predicted as class `0`.

2. **True Positives (TP)** - class `1` values **correctly** predicted as class `1`.

3. **False Positives (FP)** - class `0` values **incorrectly**  predicted as class `1`.

4. **False Negatives (FN)** - class `1` values **incorrectly**  predicted as class `0`.


||Predicted Class `0`|Predicted Class `1`|    
|-|-|-|
|Actual Class `0`|**TN = 97**|**FP = 50**|
|Actual Class `1`|**FN = 41**|**TP = 112**|

These values of confusion matrix are used for calculating precision, recall and f1-score with the below formulae:

1. **Precision** - It is the ratio of the correctly predicted positive values (TP) to the total predicted positive values (TP + FP) i.e.

$$\text{precision} = \frac{\text{TP}}{\text{TP + FP}}$$


2. **Recall** -  It is the ratio of the correctly predicted positive values (TP)values to the total values (TP + FN) i.e. 

$$\text{recall} = \frac{\text{TP}}{\text{TP + FN}}$$


3. **f1-score** - It is a harmonic mean of the precision and recall values, i.e.

$$\text{f1-score} = 2 \left( \frac{\text{precision} \times \text{recall}}{\text{precision} + \text{recall}} \right)$$
"""

# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir) # path to the SavedModel directory
tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)