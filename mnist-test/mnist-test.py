import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation
from keras.utils import np_utils
from keras.optimizers import adam

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train /255
x_test = x_test /255

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

model = Sequential()
# model = load_model('my_model.h5')

model.add(Dense(units=10, input_dim=784, activation='sigmoid'))
model.add(Dense(units=10, activation='sigmoid'))
model.add(Dense(units=10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer=adam(lr=0.001), metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=200, epochs=20)

test_result = model.evaluate(x_test, y_test)
print()
print('test accuracy is:', test_result[1])

model.save('my_model.h5')
del model