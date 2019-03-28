import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.cwb.gov.tw/V7/climate/monthlyMean/Taiwan_precp.htm'
file = pd.read_html(url)[3]
file = file.drop([13, 14], axis = 1)
file = file.loc[[3, 15, 12], :]
file = file.drop([0], axis = 1)

fileArr = np.array(file, dtype='float')
allData = {'Taipei': fileArr[0], 'Taichung': fileArr[1], 'Tainan': fileArr[2]}
months = np.arange(1, 13, 1)

plt.plot(months, allData['Taipei'])
plt.plot(months, allData['Taichung'])
plt.plot(months, allData['Tainan'])
plt.xticks(range(1, 13))
plt.legend(('Taipei', 'Taichung', 'Tainan'), loc='upper right')

plt.show()