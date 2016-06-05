import dataReader

import random
import math
import time

import numpy
import string
import pybrain

from pybrain.tools.shortcuts   import buildNetwork

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

    fnn = buildNetwork(100,30,8,24,bias=True)
    ds = pybrain.datasets.supervised.SupervisedDataset(lenY-1,1)
    for i in range(len(trainData)):
        ds.addSample(X[i],Y[i])

    trainer = pybrain.supervised.trainers.BackpropTrainer(fnn, ds, momentum = 0.1, verbose = True, weightdecay = 0.01)
    trainer.trainEpochs(epochs=100)
    out = pybrain.datasets.supervised.SupervisedDataset(lenY-1,1)

    for i in range(len(testData)):
        temp = [0]
        out.addSample(dX[i],temp)

    out = fnn.activateOnDataset(out)
    print len(out),out[0]
