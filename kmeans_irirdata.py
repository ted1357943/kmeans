import csv
import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


def dis_count(a, b):  # 計算兩點距離
    dis = (a[0]-eval(b[0]))**2 + (a[1]-eval(b[1]))**2 + \
        (a[2]-eval(b[2]))**2 + (a[3]-eval(b[3]))**2
    return format(dis, '.3f')


def equ_judge(x, y):  # 判斷兩中心點誤差多大
    val = abs((x[0]-y[0])+(x[1]-y[1])+(x[2]-y[2])+(x[3]-y[3]))
    return format(val, '.3f')


def plot(listReport, result):
    colors = ['r', 'g', 'b', 'y', 'k', 'm', 'c']
    plt.figure(figsize=(12, 8))

    # 以(SepalLength,SepalWidth)為XY軸,並以原資料三別畫圖
    plt.subplot(2, 2, 1)
    plt.xlabel("SepalLength")
    plt.ylabel("SepalWidth")
    plt.title("original data")
    for i in range(0, 50):
        plt.scatter(eval(listReport[i][0]), eval(listReport[i][1]), alpha=.8, color=colors[0],
                    label=0)
    for i in range(50, 100):
        plt.scatter(eval(listReport[i][0]), eval(listReport[i][1]), alpha=.8, color=colors[1],
                    label=1)
    for i in range(100, 150):
        plt.scatter(eval(listReport[i][0]), eval(listReport[i][1]), alpha=.8, color=colors[2],
                    label=2)

    # 以(PetalLength,PetalWidth)為XY軸,並以原資料三別畫圖
    plt.subplot(2, 2, 2)
    plt.xlabel("PetalLength")
    plt.ylabel("PetalWidth")
    plt.title("original data")
    for i in range(0, 50):
        plt.scatter(eval(listReport[i][2]), eval(listReport[i][3]), alpha=.8, color=colors[0],
                    label=0)
    for i in range(50, 100):
        plt.scatter(eval(listReport[i][2]), eval(listReport[i][3]), alpha=.8, color=colors[1],
                    label=1)
    for i in range(100, 150):
        plt.scatter(eval(listReport[i][2]), eval(listReport[i][3]), alpha=.8, color=colors[2],
                    label=2)

    # 以(SepalLength,SepalWidth)為XY軸畫出kmeans分群圖
    plt.subplot(2, 2, 3)
    plt.xlabel("SepalLength")
    plt.ylabel("SepalWidth")
    plt.title("K-means data")
    for i in range(0, eval(k)):
        for j in range(0, len(result)):
            if (result[j][4] == i):
                plt.scatter(result[j][0], result[j][1], alpha=.8, color=colors[i],
                            label=i)

    # 以(PetalLength,PetalWidth)為XY軸畫出kmeans分群圖
    plt.subplot(2, 2, 4)
    plt.xlabel("PetalLength")
    plt.ylabel("PetalWidth")
    plt.title("K-means data")
    for i in range(0, eval(k)):
        for j in range(0, len(result)):
            if (result[j][4] == i):
                plt.scatter(result[j][2], result[j][3], alpha=.8, color=colors[i],
                            label=i)

    plt.tight_layout()
    plt.show()


with open('iris.csv', newline='') as csvfile:            # 開啟 CSV 檔案
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    listReport = list(rows)

k = input("please enter cluster numbers:\n")
old_center = [[0]*5 for i in range(eval(k))]
rand_num = random.sample(range(0, len(listReport)), eval(k))  # 從資料中選k個數
ori_data = listReport

for i in range(0, eval(k)):  # 紀錄最初中心值
    s = rand_num[i]
    for q in range(0, 4):
        old_center[i][q] = eval(listReport[s][q])
    old_center[i][4] = i

flag = 0
times = 0
while (flag != eval(k)):  # 更新中心
    new_center = [[0]*5 for i in range(eval(k))]
    for j in range(0, len(listReport)):
        min = 0
        for i in range(0, eval(k)):
            if (eval(dis_count(old_center[min], listReport[j])) > eval(dis_count(old_center[i], listReport[j]))):
                min = i
        listReport[j][4] = min

    for i in range(0, eval(k)):  # 計算新中心
        sum = 0
        for j in range(0, len(listReport)):
            if (listReport[j][4] == i):
                sum = sum+1
                for q in range(0, 4):
                    new_center[i][q] = new_center[i][q]+eval(listReport[j][q])
        new_center[i][4] = i
        for q in range(0, 4):
            if (sum != 0):
                new_center[i][q] = round(new_center[i][q]/sum, 3)

    for i in range(0, eval(k)):
        if (eval(equ_judge(new_center[i], old_center[i])) < 0.01):
            flag = flag+1
        old_center[i] = new_center[i]
    times += 1
    if times > 99:
        break


result = [[0]*5 for i in range(len(listReport))]
m = 0
for i in range(0, eval(k)):                         # 將同類排在一起
    for j in range(0, len(listReport)):
        if (listReport[j][4] == i):
            for q in range(0, 4):
                result[m][q] = eval(listReport[j][q])
            result[m][4] = i
            m = m+1

plot(ori_data, result)
