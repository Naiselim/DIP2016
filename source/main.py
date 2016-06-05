import bagging_dtree
import dataDivider
import dataFilter
import dataReader
import normalization
import bagging_svm
import mar
import KNN_main
import KNN_check
import ann

alldatas,lenX,lenY = dataReader.dataRead("../data/exp2_raw_data/modfied11w.out")

newdatas = dataFilter.onlyYearAndClick(alldatas)

newdatas = normalization.max_min(newdatas)

trainData,testData = dataDivider.dataDivide(newdatas, 10)

ann.getTrain(trainData, testData)

#bagging_svm.bg_svm(trainData, testData, 1, len(trainData))

#print mar.getTrain(trainData, testData)

#KNN_check.getTrain(trainData, testData)

#print result, len(testData)
