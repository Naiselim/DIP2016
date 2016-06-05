from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import random

def bg_dt(trainData,testData,bagnum,bagsize):

    ans_list = []
    for i in testData:
        ans_list.append(0)

    lenX = len(trainData)
    lenY = len(testData)
    lenZ = len(trainData[0])

    X = np.zeros((bagsize,lenZ-1))
    y = np.zeros((bagsize,1))

    dX = np.zeros((lenY,lenZ-1))

    for i in range(bagnum):
        random.shuffle(trainData)

        for j in range(bagsize):
            for k in range(lenZ-1):
                X[j][k] = trainData[(j+i*bagnum)%lenX][k]
            y[j][0] = trainData[(j+i*bagnum)%lenX][lenZ-1]

        for j in range(lenY):
            for k in range(lenZ-1):
                dX[j][k] = testData[j][k]
            #y[j][0] = trainData[(j+i*bagnum)%lenX][lenZ-1]

# fit a CART model to the data
        model = DecisionTreeClassifier()
        model.fit(X, y)
        #print(model)
# make predictions
        #expected = y
        dY = model.predict(dX)
        for j in range(lenY):
            if dY[j]>=0:
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
