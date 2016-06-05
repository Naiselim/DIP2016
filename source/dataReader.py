import string

def dataRead(path):

    f = open(path,'r')

    #print "fuck"
    lines = f.readlines()
    #print len(lines)
    datas = []

    i = 0
    j = 0
    for line in lines:
        #line = f.readline()
        data = line.split('	')
        #print len(data)

        if(len(data) != 19):
            j += 1
            print data
        else:
            datas.append(data)
        i += 1

    lenX = len(datas)
    lenY = len(datas[0])
    #print "check ", j
    return datas,lenX,lenY


#datas, lenX, lenY = dataRead("./data/exp2_webspamdata/data.csv")
#print lenX, lenY

datas,lenX,lenY = dataRead("../data/exp2_raw_data/train11w.data")

#print lenX,lenY,datas[0],datas[1]

#only number: 1 2 3 4 5 6 7 8 9 10 11 12
