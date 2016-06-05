import bagging_dtree
import dataDivider
import dataFilter
import dataReader
import normalization
import bagging_svm
import mar

alldatas,lenX,lenY = dataReader.dataRead("../data/exp2_raw_data/modfied11w.out")

newdatas = dataFilter.dataFilter(alldatas)

newdatas = normalization.max_min(newdatas)

trainData,testData = dataDivider.dataDivide(newdatas, 5)

result = mar.getTrain(trainData, testData)

print result, len(testData)
