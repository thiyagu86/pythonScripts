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
wind,date=[],[]
minTimeGHD, maxTimeGHD = [],[]
minTimePI,maxTimePI = [],[]
userEmail=""

for row in csv_reader:
	#print(row[4],row[5])
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

averageGHD = Average(minTimeGHD)
averagePI = Average(minTimePI)
#print ("Minimum response time for getHeroData : ", min(minTimeGHD), "ms")
minTimeGHDsecs=min(minTimeGHD)/1000
print("Mininum response time for getHeroData: ",minTimeGHDsecs," secs")
#print ("Maximum response time for getHeroData : ", max(minTimeGHD), "ms")
maxTimeGHDsecs = max(minTimeGHD)/1000
print ("Maximum response time for getHeroData : ", maxTimeGHDsecs, "secs")
#print("Average response time for getHeroData  : ", round(averageGHD,2),"ms")
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
#print ("Minimum response time for priorityIncident : ", min(minTimePI),"ms")
minTimePIsecs=min(minTimePI)/1000
print ("Minimum response time for priorityIncident : ", minTimePIsecs,"secs")
#print ("Maximum response time for priorityIncident : ", max(minTimePI),"ms")
maxTimePIsecs=max(minTimePI)/1000
print ("Maximum response time for priorityIncident : ", maxTimePIsecs,"secs")
#print("Average response time for getHeroData : ", round(averagePI, 2),"ms")
AvgPISecs = round(averagePI, 2)/1000
print("Average response time for getHeroData : ", AvgPISecs,"secs")
PIData =[]
PIData.append(count)
PIData.append("priorityIncidents")
PIData.append(userEmail)
PIData.append(minTimePIsecs)
PIData.append(maxTimePIsecs)
PIData.append(AvgPISecs)
send2CSV(PIData)
