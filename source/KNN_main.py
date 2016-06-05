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

def getTrain(trainData, testData, Maxlevel):

    f = open("test.txt", "w")

    G = []
    weight = []
    alpha = []
    N = len(trainData)
    ans_list = []
    for i in range(N):
        weight.append(float(1.0/float(N)))


    for i in testData:
        ans_list.append(0)

    lenX = len(trainData)
    lenY = len(testData)
    lenZ = len(trainData[0])

    X = np.zeros((lenX,lenZ-1))
    y = np.zeros((lenX,1))

    dX = np.zeros((lenY,lenZ-1))

    for i in range(Maxlevel):
#Generate a hypothesis Ct;
        for j in range(lenX):
            for k in range(lenZ-1):
                X[j][k] = trainData[j][k]
            y[j][0] = trainData[j][lenZ-1]

        for j in range(lenY):
            for k in range(lenZ-1):
                dX[j][k] = testData[j][k]
            #y[j][0] = trainData[(j+i*bagnum)%lenX][lenZ-1]

# fit a CART model to the data
        model = neighbors.KNeighborsClassifier(algorithm='kd_tree')
        model.fit(X, y)
        #print(model)
# make predictions
        #expected = y
        dY = model.predict(X)
#Compute the error rate Et :Et = sum of the weights of all misclassified samples;
        error = 0.0
        for j in range(lenX):
            #print >>f,dY[j],trainData[j][lenZ-1]
            if dY[j] <= 0 and trainData[j][lenZ-1] > 0:
                #print "enter"
                error += weight[j]
            elif dY[j] >= 0 and trainData[j][lenZ-1] < 0:
                #print "enter"
                error += weight[j]

        error = max(error, 1e-10)
        #print "error: %.5f" % error
        at = (math.log(1.0-error) - math.log(error))/2

#Update the weight of each example:
        wsum = 0.0
        for j in range(lenX):
            if dY[j]*trainData[j][lenZ-1] < 0:
                weight[j] = weight[j] * math.exp(-1.0*at)
            else:
                weight[j] = weight[j] * math.exp(at)
            wsum += weight[j]

        for j in range(lenX):
            weight[j] /= wsum


        G.append(model)
        alpha.append(at)
        #if error < 1e-10:
        #    print "early exit in %d weak classifers" % (i)
        #    break

#predict
    for i in range(len(G)):
        for j in range(lenY):
            for k in range(lenZ-1):
                dX[j][k] = testData[j][k]

        dY = G[i].predict(dX)
        for j in range(lenY):
            if dY[j] >= 0:
                ans_list[j] += 1
            else:
                ans_list[j] -= 1

    fp = 0
    tp = 0
    fn = 0
    tn = 0
    for i in range(len(ans_list)):
        if ans_list[i] >= 0:
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
