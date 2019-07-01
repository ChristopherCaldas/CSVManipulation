#RingLead
#Christopher Caldas


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
    header = next(csv_f)
    fillCount = [0] * len(header)
    numRows = 0
    for row in csv_f:
        numRows += 1
        colCount = 0
        while(colCount < len(header)):
            if(row[colCount] != '' and row[colCount] != 'n/a'):
                fillCount[colCount] += 1
            colCount += 1
    f.close()
    return(header,fillCount,numRows)

#Creates a file to display the fill percentages from a given file
def fillRateSingleFile(f1,output):
    fileData = fileFillRate(f1)
    fillPercentage = [round(x / fileData[2],2) for x in fileData[1]]
    transposedFile = fileData[0],fileData[1], fillPercentage
    transposedFile = matrixTranspose(transposedFile)
    currentDate = (datetime.date.today().strftime("%B %d, %Y")).replace(",","")
    with open(output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([currentDate])
        writer.writerow(["Fields","Fill Count","Fill Percentage"])
        [writer.writerow(row) for row in transposedFile]

#Finds the fill rates for two files and finds the difference of the fill rates. Outputs into format designated by Maria
def compareFiles(f1,f2,output):
    output1 = fileFillRate(f1)
    output2 = fileFillRate(f2)
    if(output1[0] == output2[0]):
        fillRateDifference = [a - b for a, b in zip(output1[1], output2[1])]
        transposedFile = matrixTranspose([output1[0],output1[1],output2[1],fillRateDifference])
        transposedFile[0] = transposedFile[0] + (sum(fillRateDifference),)
        currentDate = (datetime.date.today().strftime("%B %d, %Y")).replace(",","")
        with open(output, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([currentDate])
            writer.writerow(["Fields","New","Old","New-Old","Sum of New - Old: "])
            [writer.writerow(row) for row in transposedFile]
    else:
        print("ERROR:Files have different headers")

#compareFiles("D:/CSVFillRateTest.csv","D:/CSVFillRateTest2.csv","D:/output.csv ")
fillRateSingleFile("D:/LiveDataRaw.csv","D:/LiveDataAnalysis.csv")
