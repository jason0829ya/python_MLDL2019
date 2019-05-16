from keras.datasets import imdb                 # data
from keras.optimizers import adam
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM                   # RNN layer
from keras.layers import Embedding              # 壓縮文字資料
from keras.preprocessing import sequence        # 文字資料前處理器

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

x_train = sequence.pad_sequences(x_train, maxlen=150)
x_test = sequence.pad_sequences(x_test, maxlen=150)


word_dim = 5
num_LSTM_cell = 4

model = Sequential()
model.add(Embedding(10000, word_dim))
model.add(LSTM(num_LSTM_cell))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer=adam(lr=0.001), metrics=['accuracy'])
model.summary()

model.fit(x_train, y_train, batch_size=32, epochs=3)

score = model.evaluate(x_test, y_test)
print(f'testing data accuracy is ${score[1]}')