import string

import dataReader

def dataFilter(datas):
#1 2 3 4 5 6 7 8 9 10 11 12 -3 -2 -1
    newdatas = []

    for data in datas:
        newdata = []
        for i in range(12):
            if data[i+1]=='':
                newdata.append(0)
            else:
                newdata.append(string.atof(data[i+1]))

        for i in range(2):
            if data[-i-2]!='':
                newdata.append(string.atof(data[-i-2]))
            else:
                newdata.append(0)

        if data[-1] == '0\n':
            newdata.append(-1)
        else:
            newdata.append(1)

        newdatas.append(newdata)

    return newdatas

#datas,lenX,lenY = dataReader.dataRead("../data/exp2_raw_data/modfied11w.out")
#newdatas = dataFilter(datas)
#print len(newdatas),len(newdatas[0])
