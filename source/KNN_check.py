import dataReader

import random
import math
import time

import numpy
import string

import numpy as np
from sklearn import neighbors
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

def getTrain(trainData, testData):

    lenX = len(trainData)
    lenY = len(testData)
    lenZ = len(trainData[0])

    X = np.zeros((lenX,lenZ-1))
    y = np.zeros((lenX,1))

    dX = np.zeros((lenY,lenZ-1))

    for j in range(lenX):
        for k in range(lenZ-1):
            X[j][k] = trainData[j][k]
        y[j][0] = trainData[j][lenZ-1]

    for j in range(lenY):
        for k in range(lenZ-1):
            dX[j][k] = testData[j][k]

    model = neighbors.KNeighborsClassifier(algorithm='kd_tree')
    model.fit(X, y)
        #print(model)
# make predictions
        #expected = y
    dY = model.predict(dX)

    fp = 0
    tp = 0
    fn = 0
    tn = 0

    for i in range(lenY):
        if dY[i] >= 0:
            if testData[i][-1] == 1:
                tp += 1
            else:
                fn += 1
        else:
            if testData[i][-1] == 1:
                fp += 1
            else:
                tn += 1

    print "result: fp: %d tp: %d fn: %d tn: %d" % (fp,tp,fn,tn)
    return [fp,tp,fn,tn]
