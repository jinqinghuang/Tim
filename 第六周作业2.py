'''
name: 黄锦清
student number: 1619100043
function：请尝试用大家学过的数据序列，生成一个CSV文件
'''



import csv

with open("test.csv","w",newline='') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(["No.","Name","Age","Score"])
    writer.writerows([[1,'mayi',18,99],[2,'jack',21,89],[3,'tom',25,95],[4,'rain',19,80],[5,'hanmeimei',23,81]])
with open("test.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print (line)
