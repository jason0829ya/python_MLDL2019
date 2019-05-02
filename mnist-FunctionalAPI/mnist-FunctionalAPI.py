from keras.datasets import mnist
from keras.models import load_model, Model
from keras.layers import Dense, Input, concatenate
from keras.utils import np_utils
from keras.optimizers import adam

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train /255
x_test = x_test /255

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

input_x = Input(shape=(784,))

# function_layer_1 = Dense(10, activation='sigmoid')
# function_layer_2 = Dense(10, activation='sigmoid')
# function_layer_3 = Dense(10, activation='softmax')

# buffer_1 = function_layer_1(input_x)
# buffer_2 = function_layer_2(buffer_1)
# output_y = function_layer_3(buffer_2)

function_1 = Dense(10, activation='sigmoid')
function_2 = Dense(5, activation='sigmoid')
function_3 = Dense(5, activation='relu')
function_4 = Dense(10, activation='softmax')

buffer_1 = function_1(input_x)
buffer_2 = function_2(buffer_1)
buffer_3 = function_3(buffer_1)
buffer_4 = concatenate([buffer_2, buffer_3])
output_y = function_4(buffer_4)

model = Model(input_x, output_y)
model.summary()
model.compile(loss='categorical_crossentropy', optimizer=adam(lr=0.001), metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=200, epochs=20)
test_result = model.evaluate(x_test, y_test)
print()
print('test accuracy is:', test_result[1])