import os
os.system("cls")
try:
    os.mkdir("output_by_subject")
except FileExistsError:
    pass
try:
    os.mkdir("output_individual_roll")
except FileExistsError:
    pass

# Function which sets headers and data of each file of each folder
checkForSchema=0
def addDataToCorrespFile(type,name,data,methods):
    check=0
    if(type==1):
        filename="./output_individual_roll/"+name+".csv"
    else:
        filename="./output_by_subject/"+name+".csv"
    file = open(filename, methods)
    for i in data:
        if(check):
            file.write(',')
        file.write(i)
        check+=1
    file.close()

# Function which extracts the number of unique students and subjects and creates blank file for each
# and sets headers of each file
def setSchema_for_each_file():
    global checkForSchema
    if(checkForSchema==1):
        return
    checkForSchema=1
    f=open('regtable_old.csv', 'r')
    uniqueRoll = set()
    uniqueSubject = set()
    results = ["rollno","register_sem","subno","sub_type\n"]
    for line in f:
        if(line.split(',')[0] != "rollno"):
            uniqueRoll.add(line.split(',')[0])
            uniqueSubject.add(line.split(',')[3])
            
    for i in uniqueRoll:
        addDataToCorrespFile(1,i,results,"w")       # Sets headers of each file of output_individual_roll
    for i in uniqueSubject:
        addDataToCorrespFile(2,i,results,"w")       # Sets headers of each file of output_by_subject
    f.close()


# Function which extracts data from given csv file and add it to corresponding file of corresponding folder
def output_by_subject():
    setSchema_for_each_file()
    f=open('regtable_old.csv', 'r')
    for data in f:
        studentData = data.split(',');
        if(studentData[0]=="rollno"):
            continue
        results = [studentData[0],studentData[1],studentData[3],studentData[8]]
        addDataToCorrespFile(2,results[2],results,"a")      # adds data of each file of output_by_subject
    f.close()

def output_individual_roll():
    setSchema_for_each_file()
    f=open('regtable_old.csv', 'r')
    for data in f:
        studentData = data.split(',');
        if(studentData[0]=="rollno"):
            continue
        results = [studentData[0],studentData[1],studentData[3],studentData[8]]
        addDataToCorrespFile(1,results[0],results,"a")      # adds data of each file of output_individual_roll
    f.close()

# Function call made
output_by_subject()
output_individual_roll()