import csv
import random
import matplotlib.pyplot as plt
import numpy as np
import cv2


def init(ori_data, k):  # 初始化k個群心(從原資料任取k筆)
    temp = ori_data.reshape(-1, k)
    old_center = temp[np.random.choice(
        temp.shape[0], size=k, replace=False), :]
    return old_center


def dis_count(a, b):                # 計算2點間距離
    dis = (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2
    return format(dis, '.1f')


def point_count(ori_data, old_center, k, hight, width):  # 計算各點與各群心距離並分群
    for i in range(hight):
        for j in range(width):
            min = dis_count(old_center[0], ori_data[i][j])
            ori_data[i][j][3] = 0
            for m in range(0, k):
                #print(m, ' dis:', dis_count(old_center[m], ori_data[i][j]))
                if (eval(dis_count(old_center[m], ori_data[i][j])) < eval(min)):
                    min = dis_count(old_center[m], ori_data[i][j])
                    ori_data[i][j][3] = m
            # print(ori_data[i][j])
            # print('\n')


def update_center(ori_data, new_center, k, hight, width):
    for m in range(k):
        sum = 0
        for i in range(hight):
            for j in range(width):
                if (ori_data[i][j][3] == m):
                    sum += 1
                    new_center[m][0] += ori_data[i][j][0]
                    new_center[m][1] += ori_data[i][j][1]
                    new_center[m][2] += ori_data[i][j][2]
        if (sum != 0):
            new_center[m][0] /= sum
            new_center[m][1] /= sum
            new_center[m][2] /= sum


def center_compare(old_center, new_center, k):
    flag = 0
    for m in range(k):
        if ((abs(old_center[m][0]-new_center[m][0])+abs(old_center[m][1]-new_center[m][1])+abs(old_center[m][2]-new_center[m][2])) == 0):
            flag += 1
    return flag


img = cv2.imread('./test_picture/test2.jpg')  # 讀取圖片
img = cv2.resize(img, (480, 360))  # (img.shape[1],img.shape[0])
k = eval(input("please enter cluster numbers:\n"))

ori_data = np.zeros((img.shape[0], img.shape[1], 4), dtype=int)
for i in range(img.shape[0]):  # 讀取各像素點RGB值
    for j in range(img.shape[1]):
        ori_data[i][j][0] = img[i][j][0]
        ori_data[i][j][1] = img[i][j][1]
        ori_data[i][j][2] = img[i][j][2]
        ori_data[i][j][3] = 0

old_center = init(ori_data, k)

times = 0
while (times < 300):
    new_center = np.zeros((k, 4), dtype=int)
    point_count(ori_data, old_center, k, img.shape[0], img.shape[1])
    update_center(ori_data, new_center, k, img.shape[0], img.shape[1])
    times += 1
    if (center_compare(old_center, new_center, k) == k):
        break
    old_center = new_center
print(times)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for m in range(k):
            if (ori_data[i][j][3] == m):
                img[i][j][0] = new_center[m][0]
                img[i][j][1] = new_center[m][1]
                img[i][j][2] = new_center[m][2]

cv2.imshow('My Image', img)
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
