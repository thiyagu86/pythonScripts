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
minTimeCSR = []
minTimeBS = []
minTimeCI = []
minTimeCL = []
minTimeGI = []
minTimeSR = []
minTimeSRR = []
minTimePSR = []
minTimeGSR = []
minTimeGDJM = []

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
		print("SNo: {}, apiName: {}, userEmail: {}, MinRspTime: {},MaxRspTime: {},AvgRspTime: {}".format(csvdata[0],csvdata[1],csvdata[2],csvdata[3],csvdata[4],csvdata[5]))
		csvfile.close()

def buildCSVdata(apiId,inputList):
	global count
	global userEmail
	if inputList:
		minTimesecs = min(inputList)/1000
		maxTimesecs = max(inputList)/1000
		averageTime = Average(inputList)
		AvgTimeSecs = round(averageTime,2)/1000
	else:
		return

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
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "incidentsReport"):
		try:
			minTimeIR.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "incidents"):
		try:
			minTimeI.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "createServiceRequest"):
		try:
			minTimeCSR.append(float(row[4]))
			#userEmail = row[5]
		except ValueError:
			print ("error","on line",row)	
	elif(row[1]== "businessServices"):
		try:
			minTimeBS.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "catalogueItems"):
		try:
			minTimeCI.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "codeList"):
		try:
			minTimeCL.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "getIncident"):
		try:
			minTimeGI.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "serviceRequests"):
		try:
			minTimeSR.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "serviceRequestReport"):
		try:
			minTimeSRR.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "priorityServiceRequests"):
		try:
			minTimePSR.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "getServiceRequest"):
		try:
			minTimeGSR.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)
	elif(row[1]== "getDynamicJourneyMetadata"):
		try:
			minTimeGDJM.append(float(row[4]))
			userEmail = row[5]
		except ValueError:
			print ("error","on line",row)

buildCSVdata("getHeroData",minTimeGHD)
buildCSVdata("priorityIncidents",minTimePI)
buildCSVdata("incidentsReport",minTimeIR)
buildCSVdata("incidents",minTimeI)
buildCSVdata("createServiceRequest",minTimeCSR)
buildCSVdata("businessServices",minTimeBS)
buildCSVdata("catalogueItems",minTimeCI)
buildCSVdata("codeList",minTimeCL)
buildCSVdata("getIncident",minTimeGI)
buildCSVdata("serviceRequests",minTimeSR)
buildCSVdata("serviceRequestReport",minTimeSRR)
buildCSVdata("priorityServiceRequests",minTimePSR)
buildCSVdata("getServiceRequest",minTimeGSR)
buildCSVdata("getDynamicJourneyMetadata",minTimeGDJM)