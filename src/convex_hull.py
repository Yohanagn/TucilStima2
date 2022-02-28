from math import degrees
import numpy as np

def quickhull(array, p1, p2, point): ##fungsi untuk menentukan apakah sebuah titik berada di sebelah kiri atau kanan garis pembagi
    x1 = array[p1][0]
    y1 = array[p1][1]
    x2 = array[p2][0]
    y2 = array[p2][1]
    x3 = array[point][0]
    y3 = array[point][1]
    return x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3

def besar_sudut(A, B, C):
    sudut_ba = A - B
    sudut_bc = C - B
    cos_theta = np.dot(sudut_ba, sudut_bc)/(np.linalg.norm(sudut_ba)*np.linalg.norm(sudut_bc))

    cos_theta = np.clip(cos_theta, -1, 1)
    
    return np.degrees(np.arccos(cos_theta))


def finding_maxmin(array):
    x = []
    for i in range(len(array)):
        x.append(array[i][0])
    Min = min(x)
    Max = max(x)

    idxMin = 0
    flag = True
    while idxMin < len(array) and flag:
        if array[idxMin][0] == Min:
            flag = False
        else: idxMin += 1
        
    idxMax = 0
    flag = True
    while (idxMax < len(array) and flag):
        if array[idxMax][0] == Max:
            flag = False
        else: idxMax += 1
    
    return (idxMin, idxMax)

def convexhull(vertices):
    arr = np.array(vertices).astype(float)
    
    p1, p2 = finding_maxmin(arr)
    
    left = []
    right = []

    for i in range(len(arr)):
        if quickhull(arr, p1, p2, i) > 0 and i != p1 and i != p2:
            left.append(i)
        elif quickhull(arr, p1, p2, i) < 0 and i != p1 and i != p2:
            right.append(i)

    left_recursion = convexhull2(arr, left, p1, p2)
    right_recursion = convexhull2(arr, right, p2, p1)
    return left_recursion + right_recursion


def convexhull2(arr, array, p1, p2): #menentukan pasangan indeks titik pada garis pembentuk bidang
    if len(array) == 0:
        if p1 != p2:
            return [[p1, p2]]
        else:
            return []
    else:   # kondisi dimana ada titik di sisi garis
        degrees = []
        for i in range(len(array)):
            if p1 != p2 and p1 != array[i] and p2 != array[i]:
                derajat2 = besar_sudut(arr[p2], arr[p1], arr[array[i]])
            else:
                derajat2 = 0
            degrees.append(derajat2)
        point = array[degrees.index(max(degrees))]

        point1 = []
        for i in range(len(array)):
            if quickhull(arr, p1, point, array[i]) > 0 and array[i] != p1 and array[i] != p2:
                point1.append(array[i])
        point2 = convexhull2(arr, point1, p1, point)

        point3 = []
        for i in range(len(array)):
            if quickhull(arr, point, p2, array[i]) > 0 and array[i] != p1 and array[i] != p2:
                point3.append(array[i])
        point4 = convexhull2(arr, point3, point, p2)

        return point2 + point4

