for i in range(10):
    file = open("printoff.txt", "r")
    lineList = file.readlines()
    file.close()
    first = int(lineList[0])
    last = int(lineList[len(lineList)-1])