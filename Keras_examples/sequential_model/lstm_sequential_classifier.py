# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 下午3:01
# @Author  : Azrael.Bai
# @File    : lstm_sequential_classifier.py
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM

import numpy as np

x_train = np.random.random((1000, 20))
y_train = np.random.randint(2, size=(1000, 1))
x_test = np.random.random((100, 20))
y_test = np.random.randint(2, size=(100, 1))

model = Sequential()
model.add(Embedding(20, output_dim=256)) # max_features没有预定义,根据数据形式改变
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=16, epochs=10)
score = model.evaluate(x_test, y_test, batch_size=16)

print score
print model.predict(x_train[1:2])