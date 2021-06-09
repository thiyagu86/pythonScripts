import csv
IsFirstTime=True
count=1
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

averageGHD = Average(minTimeGHD)
averagePI = Average(minTimePI)
averageIR = Average(minTimeIR)
averageI = Average(minTimeI)


minTimeGHDsecs=min(minTimeGHD)/1000
print("Mininum response time for getHeroData: ",minTimeGHDsecs," secs")
maxTimeGHDsecs = max(minTimeGHD)/1000
print ("Maximum response time for getHeroData : ", maxTimeGHDsecs, "secs")
AvgGHDSecs = round(averageGHD,2)/1000
print ("Average response time for getHeroData : ", AvgGHDSecs, "secs")
GHDData = []
GHDData.append(count)
GHDData.append("getHeroData")
GHDData.append(userEmail)
GHDData.append(minTimeGHDsecs)
GHDData.append(maxTimeGHDsecs)
GHDData.append(AvgGHDSecs)
send2CSV(GHDData)
count += 1

minTimePIsecs=min(minTimePI)/1000
print ("Minimum response time for priorityIncident : ", minTimePIsecs,"secs")
#print ("Maximum response time for priorityIncident : ", max(minTimePI),"ms")
maxTimePIsecs=max(minTimePI)/1000
print ("Maximum response time for priorityIncident : ", maxTimePIsecs,"secs")
#print("Average response time for getHeroData : ", round(averagePI, 2),"ms")
AvgPISecs = round(averagePI, 2)/1000
print("Average response time for priorityIncident : ", AvgPISecs,"secs")
PIData =[]
PIData.append(count)
PIData.append("priorityIncidents")
PIData.append(userEmail)
PIData.append(minTimePIsecs)
PIData.append(maxTimePIsecs)
PIData.append(AvgPISecs)
send2CSV(PIData)
count += 1

minTimeIRsecs=min(minTimeIR)/1000
print ("Minimum response time for incidentsReport : ", minTimeIRsecs,"secs")
maxTimeIRsecs=max(minTimeIR)/1000
print ("Maximum response time for incidentsReport : ", maxTimeIRsecs,"secs")
AvgIRSecs = round(averageIR, 2)/1000
print("Average response time for incidentsReport : ", AvgIRSecs,"secs")
IRData =[]
IRData.append(count)
IRData.append("incidentsReport")
IRData.append(userEmail)
IRData.append(minTimeIRsecs)
IRData.append(maxTimeIRsecs)
IRData.append(AvgIRSecs)
send2CSV(IRData)
count += 1

minTimeIsecs=min(minTimeI)/1000
print ("Minimum response time for incidents : ", minTimeIsecs,"secs")
maxTimeIsecs=max(minTimeI)/1000
print ("Maximum response time for incidents : ", maxTimeIsecs,"secs")
AvgISecs = round(averageI, 2)/1000
print("Average response time for incidents : ", AvgISecs,"secs")
IData =[]
IData.append(count)
IData.append("incidents")
IData.append(userEmail)
IData.append(minTimeIsecs)
IData.append(maxTimeIsecs)
IData.append(AvgISecs)
send2CSV(IData)