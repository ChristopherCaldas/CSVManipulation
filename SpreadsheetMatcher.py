#RingLead
#Christopher Caldas
import csv

#Goes through all data points in two spreadsheets with the same format, and finds if the values are equal or not.
def spreadsheetMatch(f1,f2,outputFile):
    first = open(f1,encoding = "UTF-8")
    second = open(f2,encoding = "UTF-8")
    csv_f1 = csv.reader(first)
    csv_f2 = csv.reader(second)
    header1 = next(csv_f1)
    header2 = next(csv_f2)

    #Ensures mis-matched fields have not been accidently submitted
    if(not header1 == header2 ):
        print("Headers are different, matching will be inaccurate")

    #Iterates through the two files row-by-row and finds matches
    output = [header1]
    for row in csv_f1:
        currentMatcher = []
        for(i,j) in zip(row,next(csv_f2)):
            if(i == j):
                currentMatcher.append("MATCH",)
            else:
                currentMatcher.append("NO-MATCH",)
        output.append(currentMatcher)
    first.close()
    second.close()
    #Pushes output to given file
    with open(outputFile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        [writer.writerow(row) for row in output]



spreadsheetMatch("D:/Owler(old).csv","D:/DBUSA(old).csv","D:/outputMatch.csv")
