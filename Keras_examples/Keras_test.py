# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 下午3:17
# @Author  : Azrael.Bai
# @File    : Keras_test.py

from keras.models import Sequential
from keras.layers import Dense
import numpy as np


x=np.array([[0,1,0],[0,0,1],[1,3,2],[3,2,1]])
y=np.array([0,0,1,1]).T
simple_model=Sequential()
simple_model.add(Dense(5,input_shape=(x.shape[1],),activation='relu',name='layer1'))
simple_model.add(Dense(4,activation='relu',name='layer2'))
simple_model.add(Dense(1,activation='sigmoid',name='layer3'))
simple_model.compile(optimizer='sgd',loss='mean_squared_error')
simple_model.fit(x,y,epochs=10000)
print simple_model.predict(x[0:1])
quit()

from keras.models import Sequential
from keras.layers import Dense, Activation

# Sequential模型如下
model = Sequential()
# 将一些网络层通过.add()堆叠起来，就构成了一个模型：
model.add(Dense(64, input_dim=2)) # input_dim输出层特征数
model.add(Activation("relu"))
model.add(Dense(1)) # 最后一层,等于输出层特征数
model.add(Activation("softmax"))

# 完成模型的搭建后，我们需要使用.compile()方法来编译模型：
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy']) # loss中categorical_crossentropy和mean_squared_error的区别,接受的数据是不一样的

# from keras.optimizers import SGD
# model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True))

import numpy as np
x_train = np.array([[0,1],[1,2]])
y_train = np.array([[1],[2]])
x_test = np.array([[1,4],[2,2]])
y_test = np.array([[3],[2]])

# 完成模型编译后，我们在训练数据上按batch进行一定次数的迭代来训练网络
model.fit(x_train, y_train, epochs=5, batch_size=32)
# 当然，我们也可以手动将一个个batch的数据送入网络中训练，这时候需要使用：
# model.train_on_batch(x_batch, y_batch)

# 随后，我们可以使用一行代码对我们的模型进行评估，看看模型的指标是否满足我们的要求：
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

# 或者，我们可以使用我们的模型，对新的数据进行预测：
classes = model.predict(x_test, batch_size=128)
p_classes = model.predict_classes(x_test, batch_size=32)
p_proba = model.predict_proba(x_test, batch_size=32)

print p_classes
print p_proba