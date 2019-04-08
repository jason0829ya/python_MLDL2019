import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR

url = 'https://www.basketball-reference.com/leagues/NBA_2018.html'
fileEast = pd.read_html(url)[0]
fileWest = pd.read_html(url)[1]

#fileEast = fileEast.loc[:, ['W/L%', 'PS/G']]
X_train= np.array(fileEast[['PS/G', 'PA/G']], dtype='float')  # team points & opponent points per game of eastern team
X_test = np.array(fileWest[['PS/G', 'PA/G']], dtype='float')  # team points & opponent points per game of western team
Y_train = np.array(fileEast['W/L%'], dtype='float') # win rate of eastern team
Y_test = np.array(fileWest['W/L%'], dtype='float')  # win rate of western team


Y_train = Y_train.reshape(len(Y_train), 1)
Y_test = Y_test.reshape(len(Y_test), 1)

my_model = LR()
my_model.fit(X_train, Y_train)
output = my_model.predict(X_test)

rankWest = np.linspace(1, 15, 15)
plt.scatter(rankWest, output)
plt.scatter(rankWest, Y_test)
plt.xticks(range(1, 16))
plt.legend(('predict', 'data'), loc='upper-right')
plt.xlabel('team-rank')
plt.ylabel('win-rate')

plt.show()