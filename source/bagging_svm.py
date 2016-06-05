import svm_data_print
import random
import os
import string

def bg_svm(trainData,testData,bagnum,bagsize):
    ans_list = []
    for i in testData:
        ans_list.append(0)

    xx = len(testData[0])
    for i in range(bagnum):
        random.shuffle(trainData)
        svm_data_print.run(trainData, i*bagsize, bagsize, "svmdata.txt")
        svm_data_print.run(testData, 0, len(testData), "svmtestdata.txt")
        os.system("./svm_learn -c 0.5 svmdata.txt bagmodel.train")
        os.system("./svm_classify -f 1 svmtestdata.txt bagmodel.train svmanswer.txt")
        fout = open("svmanswer.txt","r")
        lines = fout.readlines()
        j = 0
        for line in lines:
            x = string.atof(line)
            if x > 0:
                ans_list[j] += 1
            else:
                ans_list[j] -= 1
            j += 1
        fout.close()

    for i in range(len(ans_list)):
        if ans_list[i] >= 0:
            ans_list[i] = 1
        else:
            ans_list[i] = -1

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
