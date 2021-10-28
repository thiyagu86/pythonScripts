import csv
import os

IsFirstTime=True
count=1

delimiter = csv.excel()
delimiter.delimiter=","
file = open("task.csv")
#file=open("NotWorking.csv")
file.readline()
csv_reader=csv.reader(file,delimiter)
Contents = list(csv_reader)
UUIDList = set() #Unique UID list

#Function to write the compiled date into a csv file
def send2CSV(csvdata):
	filename = "ConsolidatedVax.csv"
	global IsFirstTime
    
	with open(filename, 'a',newline='') as csvfile:
		csvwriter = csv.writer(csvfile) 
		if(IsFirstTime == True):
			headers = [ 'Serial no','UID','Manufacturer','Date of report', 'Report [initial / follow-up]',
						'Reporter', 'Type of Report', 'Country', 'Seriousness', 'Seriousness criteria', 'Age',
						'Age Unit',	'Age Group', 'Weight', 'Gender', 'Adverse Event', 'Outcome', 'Drugs',
						'Drug Information /Suspect / Conmed / Interacting', 'Indication', 'Route', 
						'Dose/interval', 'Dose/cumulative', 'Duration', 'Start date', 'End date', 'Action taken',
						'Rechallenge', 'Dechallenge outcome information']
			csvwriter.writerow(headers)
			IsFirstTime = False
		csvwriter.writerow(csvdata)
		#print("SNo: {}, UID: {}, Manufacturer: {},Date of report: {},Report[initial/follow-up]: {},Seriousness:{},Age: {},Gender:{},AE: {},Outcome:{},DI:{},Route:{},Dose:{},Duration:{},Start Date:{}".format(csvdata[0],
			   #csvdata[1],csvdata[2],csvdata[3],csvdata[4],csvdata[8],csvdata[10],csvdata[14],csvdata[15],csvdata[16],csvdata[18],csvdata[20],csvdata[21],csvdata[23],csvdata[24]))
		csvfile.close()

#Function to build complete data for the given Var ID
def buildCSVdata(ID):
	global count
	for row in Contents:
		if(row[0] == ID):
			csvData = []
			csvData.append(count)
			csvData.append(row[0]) # UID
			csvData.append(row[36]) #Manufacturer
			csvData.append(row[1]) # Date of Report
			csvData.append(row[29]) #Report [initial/follow-up]
			csvData.append("") #Reporter
			csvData.append("") #Type of Report
			csvData.append("") #Country
			csvData.append(row[11]) #Seriousness
			csvData.append("") #Seriousness Criteria
			csvData.append(row[4]) # Age
			csvData.append("") # Age Unit
			csvData.append("") #Age group
			csvData.append("") # Weight
			csvData.append(row[6]) # Gender
			csvData.append(row[42]) #Adverse event
			if(row[9] == 'Y'): #Outcome
				csvData.append("Died")
			elif(row[11] == 'Y'):
				csvData.append("Life-Threatening")
			else:
				csvData.append("N/A")
			csvData.append("") #Drugs
			csvData.append(row[24]) #Drug information/Suspect/Conmed/Interacting
			csvData.append("") #Indication
			csvData.append(row[39]) #Route
			csvData.append(row[38]) #Dose/interval 
			csvData.append("") #Dose/cumulative
			csvData.append(row[20]) #Duration
			csvData.append(row[19]) #Start Date
			csvData.append("") #End Date
			csvData.append("") #Action Taken
			csvData.append("") #ReChallenge
			csvData.append("") #Dechallenge outcome information
			send2CSV(csvData)
			count += 1
			break #Stop collecting data for the varID from other records in the task.csv file

#Function to build unique list of var_ids as numerous duplicate entries were observed in the data set
def buildUniqList():
	for row in Contents:
		UUIDList.add(row[0])

buildUniqList()

#Iterate over the unique list of var_ids and generate data for them
for ID in UUIDList:
	if(ID != ""):
		buildCSVdata(ID)
