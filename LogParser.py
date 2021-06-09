import csv
import os
import time
import threading
#Required functionality
#Read input file ()
from csv import writer
#Global Variables
count=1
URLCount=1
IsFirstTime=True
Lock = threading.Lock()

inputFile = 'C:/Users/reach/OneDrive/Desktop/ScriptingWork/CoveRunLogs/vuser_7.log'
getHeroFp = open("getHeroData.log","w+")
getPriorityIncidentFp = open("priorityIncidents.log","w+")
incidentsReportFp = open("incidentsReport.log","w+")
incidentsFp=open("incidents.log","w+")
createServiceRequestFp=open("createServiceRequest.log","w+")

#URL files
samlssoFp=open("samlsso.log","w+")
ticketsFp=open("tickets.log","w+")

apiId1='getHeroData'
apiId2='priorityIncidents'
apiId3='incidentsReport'
apiId4='incidents'
apiId5='createServiceRequest'

apiIdList=['getHeroData','priorityIncidents','incidentsReport','incidents','createServiceRequest']

urlId1='ciamsso.pre1.ciam.vodafone.com/samlsso'
urlId2='portal/tickets'
urlIdlist=['samlsso','tickets']

#urlId1='portal/tickets'
#urlIdlist=['tickets']

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

with open(inputFile, 'r') as file:
	for line in file:
		if apiId5 in line:
			createServiceRequestFp.write(line)

getHeroFp.close()
getPriorityIncidentFp.close()
incidentsReportFp.close()
incidentsFp.close()
createServiceRequestFp.close()

#URL data
with open(inputFile, 'r') as file:
	for line in file:
		if urlId1 in line:
			samlssoFp.write(line.strip())
			samlssoFp.write("\n")
			samlssoFp.write(next(file, '').strip())
			samlssoFp.write("\n")

with open(inputFile, 'r') as file:
	for line in file:
		if urlId2 in line:
			ticketsFp.write(line.strip())
			ticketsFp.write("\n")
			ticketsFp.write(next(file, '').strip())
			ticketsFp.write("\n")

samlssoFp.close()
ticketsFp.close()


#Lines of interest for getHeroData API are transffered to getHeroData File. 
#start working on the isolating request and response times using internal ID
getHeroDatadata = 'getHeroData.log'
priorityIncidentsdata = 'priorityIncidents.log'
timestr="ms"
NA="Not applicable"

#delete temp files
def DeleteTempFiles():
    for i in apiIdList:
        filename=i+'.log'
        os.remove(filename)
        print(filename)
    for i in urlIdlist:
    	filename=i+'.log'
    	os.remove(filename)
    	print(filename)

#This function extracts metadata from the https string
def ParseUrlString(apiId,urlStr,linedata,isUrlProc):
	if(isUrlProc == True):
		linedata.append(NA) #This is for adding not applicable for email
		linedata.append(NA) #This is for adding not applicable for hash
	else:
		metadata = urlStr.split(apiId,1)[1]
		emailData=metadata.split("&p_auth",1)[0]
		email=emailData.split("=",1)[1]
		linedata.append(email)
		userhash=metadata.split("&p_auth=",1)[1]
		hash=userhash.split('\"',1)[0]
		linedata.append(hash)
		linedata.append(NA) #This is for adding not applicable cause for internal APIs
		#print(linedata)

def processLoI(apiId,line,linedata,isUrlProc=False):
	TimeTaken=line.split(' ',1)[0]
	Time = ''.join((x for x in TimeTaken if x.isdigit()))
	StrippedTime = Time.lstrip("0")
	#print(StrippedTime)
	tokens=line.split(' ')
	substr='https'
	url = [string for string in tokens if substr in string]
	urlStr = url[0]
	linedata.append(StrippedTime)
	ParseUrlString(apiId,urlStr,linedata,isUrlProc)

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

def findMatchingRespAndCause(urlId,line,tokens,linedata):
	intId = tokens[7] +' ' + tokens[8]
	reqMatch = ["Response",intId]
	filename = urlId + ".log"
	with open(filename,'r') as respFile:
		for line in respFile: 
			if all(str in line for str in reqMatch):
				unstrippedcause=next(respFile, '').strip()
				#strippedcause=unstrippedcause.lstrip(" 		  ")
				cause=unstrippedcause.rstrip("\n")
				#print("Cause:",cause)
				processLoI(urlId,line,linedata,True)
				linedata.append(cause)

def send2CSV(csvdata):

	global IsFirstTime
	global Lock
	filename = "ConsolidatedAPIdata.csv"
	Lock.acquire()
	with open(filename, 'a',newline='') as csvfile:
		csvwriter = csv.writer(csvfile) 
		if(IsFirstTime == True):
			headers = ['SerialNo','apiName', 'reqTime', 'responseTime', 'Timetaken','userEmail','userHash','cause']
			csvwriter.writerow(headers)
			IsFirstTime = False
		csvwriter.writerow(csvdata)
		csvfile.close()
	Lock.release()

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
			csvdata.append(Resplinedata[4])
			print("CsvData: ",csvdata)
			send2CSV(csvdata)
			count+=1

def buildURLCSVData(Reqlinedata,Resplinedata):
	global count
	if(len(Resplinedata) > 2):
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
		csvdata.append(Resplinedata[4])
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
					Reqlinedata=[apiId]
					processLoI(apiId,line,Reqlinedata)
					Resplinedata=[apiId]
					findMatchingResp(apiId,line,tokens,Resplinedata)
					buildCSVdata(Reqlinedata,Resplinedata)

def consolidatedUrlProcessing():
	global urlIdlist
	length = len(urlIdlist)
	for i in range(length):
		urlId = urlIdlist[i]
		filename = urlId + ".log"
		with open(filename,'r') as file:
			for line in file:
				tokens=line.split(' ')
				if 'Request' in tokens:
					Reqlinedata=[urlId]
					processLoI(urlId,line,Reqlinedata,True)
					Resplinedata=[urlId]
					findMatchingRespAndCause(urlId,line,tokens,Resplinedata)
					buildURLCSVData(Reqlinedata,Resplinedata)
				#break

#getPriorityIncidentApi()
#GetHeroDataApi()
consolidatedApiProcessing()
#time.sleep(5)
consolidatedUrlProcessing()
#DeleteTempFiles()