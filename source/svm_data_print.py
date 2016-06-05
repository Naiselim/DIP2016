def run(data,startposition,  printSize, path):

    f = open(path, "w")
    x = len(data[0])

    for i in range(printSize):
        y = (startposition + i) % len(data)
        print >>f,data[y][-1],
        for j in range(x-1):
            print >>f,"%d:%s" % (j+1,data[y][j]),
        print >>f,""
    f.close()
