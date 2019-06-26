import csv
import datetime

#Transposes a given matrix
def matrixTranspose(x):
    output = ([*zip(*x)])
    return output

#Takes a csv file and finds the fill rates for the fields from the given header
def fileFillRate(fileName):
    f = open(fileName,encoding = "UTF-8")
    csv_f = csv.reader(f)
    rowCount = 0
    rowSize = 0
    for row in csv_f:
        #Takes the first row of the file to create the header, and find the size of the output matrix
        if (rowCount == 0):
            rowSize = len(row)
            header = row
            fillCount = [0] * rowSize
        #Loops through all values which are under a field, and records all non-empty cells
        #Line 20 is responsible for the logic of what constitutes a empty cell
        else:
            colCount = 0
            while(colCount < rowSize):
                if(row[colCount] != '' and row[colCount] != 'n/a'):
                    fillCount[colCount] += 1
                colCount += 1
        rowCount += 1
    f.close()
    return(header,fillCount,rowCount)

def compareFiles(f1,f2,output):
    output1 = fileFillRate(f1)
    output2 = fileFillRate(f2)
    if(output1[0] == output2[0]):
        fillRateDifference = [a - b for a, b in zip(output1[1], output2[1])]
        transposedFile = output1[0],output1[1],output2[1],fillRateDifference
        transposedFile = matrixTranspose(transposedFile)
        transposedFile[0] = transposedFile[0] + (sum(fillRateDifference),)
        currentDate = (datetime.date.today().strftime("%B %d, %Y")).replace(",","")
        with open(output, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([currentDate])
            writer.writerow(["Fields","New","Old","New-Old","Sum of New - Old: "])
            [writer.writerow(row) for row in transposedFile]
    else:
        print("ERROR:Files have different headers")

def fillRateSingleFile(f1,output):
    fileData = fileFillRate(f1)
    fillPercentage = [round(x / fileData[2],2) for x in fileData[1]]
    transposedFile = fileData[0],fileData[1], fillPercentage
    transposedFile = matrixTranspose(transposedFile)
    with open(output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Fields","Fill Count","Fill Percentage"])
        [writer.writerow(row) for row in transposedFile]

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

def getMultipleColumns(f,names,output):
    outputMatrix = [0]*(len(names))
    columnIndex = 0
    for x in names:
        outputMatrix[columnIndex] = getColumn(f,names[columnIndex])
        columnIndex += 1
    outputMatrix = matrixTranspose(outputMatrix)
    with open(output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(names)
        [writer.writerow(row) for row in outputMatrix]


compareFiles("D:/CSVFillRateTest.csv","D:/CSVFillRateTest2.csv","D:/output.csv")
