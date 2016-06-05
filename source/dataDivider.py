import random

def dataDivide(data,part):
    #return data,data
    size = int(float(len(data))*part/(1+part))
    #    print len(trainData), size
    random.shuffle(data)

    trainData = []
    testData = []

    for i in range(len(data)):
        if i <= size:
            trainData.append(data[i])
        else:
            testData.append(data[i])
    return trainData,testData
