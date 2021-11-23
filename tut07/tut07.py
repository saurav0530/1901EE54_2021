import csv
from openpyxl import load_workbook, Workbook

# Declaring dictionaries and assigning the data to those variables from corresponding csv files
subject_data = dict()							# Stores subject info 
student_data = dict()							# Stores student info

# Function for filling subject data dictionary
with open('./course_master_dont_open_in_excel.csv') as subjectcsvFile:
	subjectReader = csv.reader(subjectcsvFile, delimiter=',', skipinitialspace=True)
	for subjects in subjectReader:
		subject_data[subjects[0]]=subjects

# Function for filling student data dictionary
with open('./studentinfo.csv') as studentcsvFile:
	studentReader = csv.reader(studentcsvFile, delimiter=',', skipinitialspace=True)
	for students in studentReader:
		student_data[students[1]] = students

# Main Function
def feedback_not_submitted():
	output_file_name = "course_feedback_remaining.xlsx"
	
	# Opening the output file and setting header
	wb = Workbook()
	ws = wb["Sheet"]
	ws.title = "Sheet1"
	header = ["rollno","register_sem","schedule_sem","subno","Name","email","aemail","contact"]
	ws.append(header)
	
	# Processing of data and saving it to output file
	with open('./course_feedback_submitted_by_students.csv') as feedbackcsvFile:
		feedbackReader = list(csv.reader(feedbackcsvFile, delimiter=',', skipinitialspace=True))
		with open('./course_registered_by_all_students.csv') as csvFile:
			reader = list(csv.reader(csvFile, delimiter=',', skipinitialspace=True))
			
			for data in reader:
				if data[0]=="rollno":
					continue

				subject = data[3]
				roll = data[0]
				ltp = list()
				student = list()
				status = [False,False,False]				# List to store if feedback is given or not in L-T-P
				ltp = subject_data[subject][2].split('-')
				
				# Finding corresponding student data from student_data dictionary
				try:
					student = student_data[roll]				
				except:
					for i in range(0,15):
						student.append("NA_IN_STUDENTINFO")
					pass

				# Finding whether feedback was given or not and assigning it to status list
				for feedback in feedbackReader:
					if(feedback[4]==subject and feedback[3]==roll):
						status[int(feedback[5])-1] = True
				else:
					for i in range(0,len(ltp)):
						if(ltp[i]!="0" and status[i]==False):
							dataToBeAdded = [
								data[0],				# Roll No
								int(data[1]),			# Registered Semester
								int(data[2]),			# Scheduled Semester
								data[3],				# Subject Code
								student[0],				# Name of student
								student[8],				# Email
								student[9],				# Secondary email
								student[10]				# Contact
							]
							ws.append(dataToBeAdded)	# Appending to output file
							break
	wb.save(output_file_name)							# Saving output file

# Calling Main function
feedback_not_submitted()