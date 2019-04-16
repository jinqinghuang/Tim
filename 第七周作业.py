'''
name: 黄锦清
student number: 1619100043
function：读取有用数据并作折线图
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
font = {'family':'SimHei'}
matplotlib.rc('font',**font)
data = pd.read_csv('35.csv')#因中文文件名无法识别所以改为了数字文件名
row = data.columns[5:20]
plt.xlabel('date')
plt.ylabel('score')
for i in range(len(data['姓名'])):
    list1 = data.iloc[i,5:20]
    plt.ylim(0,100)
    plt.plot(row,list1,'-',marker='o')
    plt.title(data.iloc[i,0])
    plt.xticks(rotation=45)
    plt.show()
