import csv
import os
import time
from threading import Thread, Lock
#Required functionality
#Read input file ()
from csv import writer
#Global Variables
count=1
URLCount=1
IsFirstTime=True
CSVLock = Lock()

#inputFile = 'C:/Users/reach/OneDrive/Desktop/ScriptingWork/CoveRunLogs/vuser_7.log'
inputFile = 'C:/Users/reach/OneDrive/Desktop/ScriptingWork/SDWANBulk/vuser_0.log'
ciaminputFile = 'C:/Users/reach/OneDrive/Desktop/ScriptingWork/CIAMLogs/vuser_combined.log'

#URL files
samlssoFp=open("samlsso.log","w+")
ticketsFp=open("tickets.log","w+")
acsFp=open("acs.log","w+")
raiseJourneyFP=open("raise-journey.log","w+")
LoginFp=open("login.log","w+")
LogoutFp=open("logout.log","w+")
keepsessionaliveFp=open("keepsessionalive.log","w+")


apiId1='getHeroData'
apiId2='priorityIncidents'
apiId3='incidentsReport'
apiId4='incidents'
apiId5='createServiceRequest'
apiId6='businessServices'
apiId7='catalogueItems'
apiId8='codeList'
apiId9='getIncident'
apiId10='serviceRequests'
apiId11='serviceRequestReport'
apiId12='priorityServiceRequests'
apiId13='getServiceRequest'
apiId14='getDynamicJourneyMetadata'

#apiIdList=['getHeroData','priorityIncidents','incidentsReport','incidents','createServiceRequest','businessServices','catalogueItems']
apiIdList=[apiId1,apiId2,apiId3,apiId4,apiId5,apiId6,apiId7,apiId8,apiId9,apiId10,apiId11,apiId12,apiId13,apiId14]
#apiIdList=[apiId9]

urlId1='ciamsso.pre1.ciam.vodafone.com/samlsso'
urlId2='portal/tickets'
urlId3='/saml/acs'
urlId4='portal/raise-journey'
urlId5='portal/login'
urlId6='portal/logout'
urlId7='ciamsso.pre1.ciam.vodafone.com/keepsessionalive?code'
urlId8='logincontext?sessionDataKey'
urlId9='v1.0/products'
urlId10='v1.0/createOrderPega'
urlId11='v1.0/ordersList'
urlId12='portal/select-organization'

urlIdlistFP=['samlsso','tickets','acs','raise-journey','login','logout','keepsessionalive','logincontext']
urlIdlistSP=['logincontext','products','createOrderPega','ordersList','select-organization']
urlIdlist = urlIdlistFP + urlIdlistSP
#urlIdlist = ['createOrderPega']

checksessionFp=open("checksession.log","w+")
logincontextFp=open("logincontext.log","w+") 
authorizeFp=open("authorize.log","w+")
clogoutFP=open("clogout.log","w+")
cloginFp=open("clogin.log","w+")
consoleFp=open("console.log","w+")
#For SDWAN
#logincontextFp gets written down anyway
productsFp=open("products.log","w+")
createOrderPegaFp=open("createOrderPega.log","w+")
ordersListFp=open("ordersList.log","w+")
selectorganizationFp=open("select-organization.log","w+")

ciamurlId1 = 'oidc/checksession'
ciamurlId2 = 'logincontext?sessionDataKey'
ciamurlId3 = 'authorize?response_type'
ciamurlId4 = 'console/logout'
ciamurlId5 = 'console/login'
ciamurlId6 = 'console\"'

CiamUrlIdList = ['checksession','logincontext','authorize','clogout','clogin','console']
#CiamUrlIdList = ['logincontext']
#urlId1='portal/tickets'
#urlIdlist=['tickets']

for apiId in apiIdList:
	filename=apiId + '.log'
	#print(filename)
	fp=open(filename,"w+")
	with open(inputFile,'r') as file:
		for line in file:
			if (apiId in line):
				fp.write(line)
	fp.close()

#URL data

#for urlId in urlIdlist:
	#filename=urlId+'.log'
	#print(filename)
	#urlfp=open(filename,"w+")
	#with open(inputFile,'r') as file:
		#for line in file:
			#if urlId in line:
				#urlfp.write(line.strip())
				#urlfp.write("\n")
				#urlfp.write(next(file, '').strip())
				#urlfp.write("\n")
	#urlfp.close()
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

with open(inputFile, 'r') as file:
	for line in file:
		if urlId3 in line:
			acsFp.write(line.strip())
			acsFp.write("\n")
			acsFp.write(next(file, '').strip())
			acsFp.write("\n")

with open(inputFile, 'r') as file:
	for line in file:
		if urlId4 in line:
			raiseJourneyFP.write(line.strip())
			raiseJourneyFP.write("\n")
			raiseJourneyFP.write(next(file, '').strip())
			raiseJourneyFP.write("\n")

with open(inputFile, 'r') as file:
	for line in file:
		if urlId5 in line:
			LoginFp.write(line.strip())
			LoginFp.write("\n")
			LoginFp.write(next(file, '').strip())
			LoginFp.write("\n")

with open(inputFile, 'r') as file:
	for line in file:
		if urlId6 in line:
			LogoutFp.write(line.strip())
			LogoutFp.write("\n")
			LogoutFp.write(next(file, '').strip())
			LogoutFp.write("\n")

with open(inputFile, 'r') as file:
	for line in file:
		if urlId7 in line:
			keepsessionaliveFp.write(line.strip())
			keepsessionaliveFp.write("\n")
			keepsessionaliveFp.write(next(file, '').strip())
			keepsessionaliveFp.write("\n")

with open(inputFile, 'r') as file:
	for line in file:
		if urlId8 in line:
			logincontextFp.write(line.strip())
			logincontextFp.write("\n")
			logincontextFp.write(next(file, '').strip())
			logincontextFp.write("\n")

with open(inputFile, 'r') as file:
	for line in file:
		if urlId9 in line:
			productsFp.write(line.strip())
			productsFp.write("\n")
			productsFp.write(next(file, '').strip())
			productsFp.write("\n")

with open(inputFile, 'r') as file:
	fileMatch = ['headers',urlId10]
	for line in file:
		if all(str in line for str in fileMatch):
			#print(line)
			createOrderPegaFp.write(line.strip())
			createOrderPegaFp.write("\n")
			createOrderPegaFp.write(next(file, '').strip())
			#print("Next:")
			#print(next(file, ''))
			createOrderPegaFp.write("\n")

with open(inputFile, 'r') as file:
	for line in file:
		if urlId11 in line:
			ordersListFp.write(line.strip())
			ordersListFp.write("\n")
			ordersListFp.write(next(file, '').strip())
			ordersListFp.write("\n")

with open(inputFile, 'r') as file:
	for line in file:
		if urlId12 in line:
			selectorganizationFp.write(line.strip())
			selectorganizationFp.write("\n")
			selectorganizationFp.write(next(file, '').strip())
			selectorganizationFp.write("\n")

samlssoFp.close()
ticketsFp.close()
acsFp.close()
raiseJourneyFP.close()
LoginFp.close()
LogoutFp.close()
keepsessionaliveFp.close()
#logincontextFp.close()
productsFp.close()
createOrderPegaFp.close()
ordersListFp.close()
selectorganizationFp.close()
#============

#CIAM URL PART
with open(ciaminputFile, 'r') as file:
	for line in file:
		if ciamurlId1 in line:
			checksessionFp.write(line.strip())
			checksessionFp.write("\n")
			checksessionFp.write(next(file, '').strip())
			checksessionFp.write("\n")

with open(ciaminputFile, 'r') as file:
	for line in file:
		if ciamurlId2 in line:
			logincontextFp.write(line.strip())
			logincontextFp.write("\n")
			logincontextFp.write(next(file, '').strip())
			logincontextFp.write("\n")

with open(ciaminputFile, 'r') as file:
	for line in file:
		if ciamurlId3 in line:
			authorizeFp.write(line.strip())
			authorizeFp.write("\n")
			authorizeFp.write(next(file, '').strip())
			authorizeFp.write("\n")

with open(ciaminputFile, 'r') as file:
	for line in file:
		if ciamurlId4 in line:
			clogoutFP.write(line.strip())
			clogoutFP.write("\n")
			clogoutFP.write(next(file, '').strip())
			clogoutFP.write("\n")

with open(ciaminputFile, 'r') as file:
	for line in file:
		if ciamurlId5 in line:
			cloginFp.write(line.strip())
			cloginFp.write("\n")
			cloginFp.write(next(file, '').strip())
			cloginFp.write("\n")

with open(ciaminputFile, 'r') as file:
	for line in file:
		if ciamurlId6 in line:
			consoleFp.write(line.strip())
			consoleFp.write("\n")
			consoleFp.write(next(file, '').strip())
			consoleFp.write("\n")

checksessionFp.close()
logincontextFp.close()
authorizeFp.close()
clogoutFP.close()
cloginFp.close()
consoleFp.close()

#SDWAN URL PART

#####
#Lines of interest for getHeroData API are transffered to getHeroData File. 
#start working on the isolating request and response times using internal ID
timestr="ms"
NA="Not applicable"

#delete temp files
def DeleteTempFiles():
    for i in apiIdList:
        filename=i+'.log'
        os.remove(filename)
        #print(filename)
    for i in urlIdlist:
    	filename=i+'.log'
    	os.remove(filename)
    	#print(filename)

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
	reqMatch = ['Response','headers',intId]
	filename = urlId + ".log"
	#print("Insided findMatchingRespAndCause",filename)
	with open(filename,'r') as respFile:
		for line in respFile: 
			if all(str in line for str in reqMatch):
				#print("Inside findMatchingRespAndCause",line)
				unstrippedcause=next(respFile, '').strip()
				#strippedcause=unstrippedcause.lstrip(" 		  ")
				Strippedcause=unstrippedcause.rstrip("\n")
				cause=Strippedcause.split(" ")[1]
				#print("Cause:",cause)
				processLoI(urlId,line,linedata,True)
				linedata.append(cause)

def send2CSV(csvdata):
	global IsFirstTime
	global CSVLock
	with CSVLock:
		filename = "ConsolidatedAPIdata.csv"
		#Lock.acquire()
		with open(filename, 'a',newline='') as csvfile:
			csvwriter = csv.writer(csvfile) 
			if(IsFirstTime == True):
				headers = ['SerialNo','apiName', 'reqTime', 'responseTime', 'Timetaken','userEmail','userHash','cause']
				csvwriter.writerow(headers)
				IsFirstTime = False
			csvwriter.writerow(csvdata)
			csvfile.close()
	#Lock.release()

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
			if Timetaken < 0:
				return
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
		if Timetaken < 0:
			return
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

def consolidatedProcessingForCIAM():
	global CiamUrlIdList
	length = len(CiamUrlIdList)
	for i in range(length):
		urlId = CiamUrlIdList[i]
		filename = urlId + ".log"
		#print(filename)
		with open(filename,'r') as file:
			for line in file:
				tokens=line.split(' ')
				reqMatch = ['Request','headers']
				if all(str in tokens for str in reqMatch):
				#if 'Request headers' in tokens:
					Reqlinedata=[urlId]
					processLoI(urlId,line,Reqlinedata,True)
					Resplinedata=[urlId]
					findMatchingRespAndCause(urlId,line,tokens,Resplinedata)
					buildURLCSVData(Reqlinedata,Resplinedata)
				#break

#getPriorityIncidentApi()
#GetHeroDataApi()
#consolidatedApiProcessing()
#time.sleep(5)
consolidatedUrlProcessing()
#time.sleep(5)
#consolidatedProcessingForCIAM()
#consolidatedProcessingForSDWAN()
DeleteTempFiles()