import dataReader

import random
import math
import time

import numpy
import string
from pyearth import Earth

def getTrain(trainData, testData):

    size_s = len(trainData)
    size_t = len(testData)
    lenY = len(testData[0])



    X = numpy.zeros((size_s,lenY-1))
    Y = numpy.zeros((size_s,1))

    z = 0

    for d in trainData:
        for j in range(lenY-1):
            X[z][j] = d[j]
        Y[z][0] = float(d[lenY-1])
        z += 1

    z = 0
    dX = numpy.zeros((size_t,lenY-1))

    for d in testData:
        for j in range(lenY-1):
            dX[z][j] = d[j]
        z += 1

    model = Earth()
    model.fit(X,Y)


    y_hat = model.predict(dX)

    corrent = 0

    for i in range(size_t):
        x1 = testData[i][lenY-1]
        x2 = y_hat[i]

        if x1 * x2 >= 0:
            corrent += 1
    return corrent
