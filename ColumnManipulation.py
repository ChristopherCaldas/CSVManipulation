#RingLead
#Christopher Caldas

import csv
#Gets an individual column from a csv file based on it's header
def getColumn(f,name):
    f = open(f,encoding = "UTF-8")
    csv_f = csv.reader(f)
    rowCount = 0
    colCount = 0
    columnLocation = -1
    outputRow = []
    for row in csv_f:
        if (rowCount != 0):
            if(columnLocation == -1):
                print("Given field not found")
            else:
                outputRow.append(row[columnLocation])
        else: 
#In the first iteration the index of the desired column is found
            for x in row:
                if(x == name):
                    columnLocation = colCount
                colCount += 1
            rowCount += 1
    f.close()
    return outputRow

def getMultipleColumns(f,names):
    outputMatrix = [0]*(len(names))
    columnIndex = 0
    for x in names:
        outputMatrix[columnIndex] = getColumn(f,names[columnIndex])
        columnIndex += 1
    return outputMatrix
