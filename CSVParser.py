import csv
IsFirstTime=True
count=1

delimiter = csv.excel()
delimiter.delimiter=","
file = open("ConsolidatedAPIdata.csv")
file.readline()
csv_reader=csv.reader(file,delimiter)
minTimeGHD = []
minTimePI = []
minTimeIR = []
minTimeI = []
userEmail= ""

def Average(dataLst):
    return sum(dataLst) / len(dataLst)

def send2CSV(csvdata):
	filename = "APIStats.csv"
	global IsFirstTime
    
	with open(filename, 'a',newline='') as csvfile:
		csvwriter = csv.writer(csvfile) 
		if(IsFirstTime == True):
			headers = ['SerialNo','apiName', 'userEmail','Minimum Response Time', 'Maximum Response time', 'Average Time Taken']
			csvwriter.writerow(headers)
			IsFirstTime = False
		csvwriter.writerow(csvdata)
		csvfile.close()

def buildCSVdata(apiId,inputList):
	global count
	minTimesecs=min(inputList)/1000
	maxTimesecs = max(inputList)/1000
	averageTime = Average(inputList)
	AvgTimeSecs = round(averageTime,2)/1000
	csvData = []
	csvData.append(count)
	csvData.append(apiId)
	csvData.append(userEmail)
	csvData.append(minTimesecs)
	csvData.append(maxTimesecs)
	csvData.append(AvgTimeSecs)
	send2CSV(csvData)
	count += 1

for row in csv_reader:
	if(row[1] == "getHeroData"):
		try:
			minTimeGHD.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "priorityIncidents"):
		try:
			minTimePI.append(float(row[4]))
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "incidentsReport"):
		try:
			minTimeIR.append(float(row[4]))
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "incidents"):
		try:
			minTimeI.append(float(row[4]))
		except ValueError:
			print ("error","on line",row)

buildCSVdata("getHeroData",minTimeGHD)
buildCSVdata("priorityIncidents",minTimePI)
buildCSVdata("incidentsReport",minTimeIR)
buildCSVdata("incidents",minTimeI)