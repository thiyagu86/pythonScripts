import csv
#Required functionality
#Read input file ()
from csv import writer
#Global Variables
count=1
IsFirstTime=True

inputFile = 'C:/Users/reach/OneDrive/Desktop/ScriptingWork/CoveRunLogs/vuser_7.log'
getHeroFp = open("getHeroData.log","w+")
getPriorityIncidentFp = open("priorityIncidents.log","w+")
incidentsReportFp = open("incidentsReport.log","w+")
incidentsFp=open("incidents.log","w+")

apiId1='getHeroData'
apiId2='priorityIncidents'
apiId3='incidentsReport'
apiId4='incidents'

apiIdList=['getHeroData','priorityIncidents','incidentsReport','incidents']

with open(inputFile, 'r') as file:
	for line in file:
		if apiId1 in line:
			getHeroFp.write(line)

with open(inputFile, 'r') as file:
	for line in file:
		if apiId2 in line:
			getPriorityIncidentFp.write(line)

with open(inputFile, 'r') as file:
	for line in file:
		if apiId3 in line:
			incidentsReportFp.write(line)

with open(inputFile, 'r') as file:
	for line in file:
		if apiId4 in line:
			incidentsFp.write(line)

getHeroFp.close()
getPriorityIncidentFp.close()
incidentsReportFp.close()
incidentsFp.close()

#Lines of interest for getHeroData API are transffered to getHeroData File. 
#start working on the isolating request and response times using internal ID
getHeroDatadata = 'getHeroData.log'
priorityIncidentsdata = 'priorityIncidents.log'
timestr="ms"

#This function extracts metadata from the https string
def ParseUrlString(apiId,urlStr,linedata):
	metadata = urlStr.split(apiId,1)[1]
	emailData=metadata.split("&p_auth",1)[0]
	email=emailData.split("=",1)[1]
	linedata.append(email)
	userhash=metadata.split("&p_auth=",1)[1]
	hash=userhash.split('\"',1)[0]
	linedata.append(hash)
	#print(linedata)

def processLoI(apiId,line,linedata):
	TimeTaken=line.split(' ',1)[0]
	Time = ''.join((x for x in TimeTaken if x.isdigit()))
	StrippedTime = Time.lstrip("0")
	#print(StrippedTime)
	tokens=line.split(' ')
	substr='https'
	url = [string for string in tokens if substr in string]
	urlStr = url[0]
	linedata.append(StrippedTime)
	ParseUrlString(apiId,urlStr,linedata)
	#print("ApiID: {}, Time: {}, Email: {}, userHash: {}".format(linedata[0],linedata[1],linedata[2],linedata[3]))

#This function will find the matching response for the given
#Request ID.
def findMatchingResp(apiId,line,tokens,linedata):
	intId = tokens[7] +' ' + tokens[8]
	reqMatch = ["Response",intId]
	filename = apiId + ".log"
	with open(filename,'r') as file:
		for line in file:
			if all(str in line for str in reqMatch):
				#print("Response line: ")
				processLoI(apiId,line,linedata)
			#else:
				#print("No response found for {}".format(reqMatch))

def send2CSV(csvdata):
	filename = "ConsolidatedAPIdata.csv"
	global IsFirstTime
    
	with open(filename, 'a',newline='') as csvfile:
		csvwriter = csv.writer(csvfile) 
		if(IsFirstTime == True):
			headers = ['SerialNo','apiName', 'reqTime', 'responseTime', 'Timetaken','userEmail','userHash']
			csvwriter.writerow(headers)
			IsFirstTime = False
		csvwriter.writerow(csvdata)
		csvfile.close()

def buildCSVdata(Reqlinedata,Resplinedata):
	global count
	if(len(Resplinedata) > 2):
		if((Reqlinedata[2] == Resplinedata[2]) and (Reqlinedata[3] == Resplinedata[3])):
			#print("Request {}: Api name: {}, Req time: {}, Rsp Time: {}, user-email:{}, userhash:{}".format(count,Reqlinedata[0],Reqlinedata[1],Resplinedata[1],Resplinedata[2],Resplinedata[3]))
			csvdata = []
			csvdata.append(count)
			csvdata.append(Reqlinedata[0])
			ReqTimeInt = int(Reqlinedata[1])
			#ReqTimeSec = ReqTimeInt//1000
			csvdata.append(ReqTimeInt)
			RspTimeInt = int(Resplinedata[1])
			#RspTimeSec = RspTimeInt//1000
			csvdata.append(RspTimeInt)
			Timetaken = RspTimeInt-ReqTimeInt
			csvdata.append(Timetaken)
			csvdata.append(Resplinedata[2])
			csvdata.append(Resplinedata[3])
			print("CsvData: ",csvdata)
			send2CSV(csvdata)
			count+=1

def consolidatedApiProcessing():
	global apiIdList
	length = len(apiIdList)
	for i in range(length):
		apiId = apiIdList[i]
		filename=apiId + ".log"
		with open(filename,'r') as file:
			for line in file:
				#Extract Request metadata here itself before trying to find matching reponse. 
				tokens=line.split(' ')
				if 'Request' in tokens:
					#print("Request line: ",line)
					Reqlinedata=[apiId]
					#print("=========Request data=================")
					processLoI(apiId,line,Reqlinedata)
					Resplinedata=[apiId]
					#print("=========Response data=================")
					findMatchingResp(apiId,line,tokens,Resplinedata)
					buildCSVdata(Reqlinedata,Resplinedata)

#getPriorityIncidentApi()
#GetHeroDataApi()
consolidatedApiProcessing()