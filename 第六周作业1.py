'''
name: 黄锦清
student number: 1619100043
function：随机产生50个数字，存一个列表中 list，然后从小到大排序，
然后写入文件，然后从文件中读取出来文件内容，然后反序，在追加到文件的下一行中
'''


import random 
f = open('test.txt', 'w')
raw =[]
for i in range(50):
    raw.append(random.randint(0,100))
raw.sort()
for j in range(50):
    f.write(str(raw[j])+ ' ')
f.close()
f = open('test.txt', 'r+')
a = f.read().split()
a.reverse()
f.write('\n')
for i in a :
    f.write(str(i)+' ')
f.close()
f = open('test.txt', 'r+')
print(f.read())