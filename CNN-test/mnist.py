import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Activation
from keras.utils import np_utils
from keras.optimizers import adam

(x_train, y_train), (x_test, y_test) = mnist.load_data()

## CNN 的 input size 是 28, 28, 1
x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)
x_train = x_train /255
x_test = x_test /255

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

model = Sequential()

model.add(Conv2D(4, (5, 5), padding='same', input_shape=(28, 28, 1)))
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Conv2D(8, (5, 5), padding='same'))
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(16, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer=adam(lr=0.001), metrics=['accuracy'])

model.summary()

model.fit(x_train, y_train, batch_size=256, epochs=10)

test = model.evaluate(x_test, y_test)
print('test accuracy is:', test[1])