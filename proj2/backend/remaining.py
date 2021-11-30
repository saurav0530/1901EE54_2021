import csv,sys
from enum import auto
from reportlab.lib import colors
from reportlab.lib.pagesizes import A3,A4, landscape
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle, Frame,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus.flowables import Spacer, TopPadder
from datetime import datetime

from reportlab.platypus.frames import ShowBoundaryValue


roll = dict()
subject = dict()

months = {
    '01':'Jan',
    '02':'Feb',
    '03':'Mar',
    '04':'Apr',
    '05':'May',
    '06':'Jun',
    '07':'Jul',
    '08':'Aug',
    '09':'Sep',
    '10':'Oct',
    '11':'Nov',
    '12':'Dec',
}


cred = {
    'AA':10,'AA*':10,
    'AB':9,'AB*':9,
    'BB':8,'BB*':8,
    'BC':7,'BC*':7,
    'CC':6,'CC*':6,
    'CD':5,'CD*':5,
    'DD':4,'DD*':4,
    'F':0,'F*':0,
    'I':0,'I*':0,
}
course = {
    'CS':'Computer Science and Engineering',
    'EE':'Electrical Engineering',
    'ME':'Mechanical Engineering',
    'CE':'Civil Engineering',
    'CB':'Chemical and Biochemical Engineering',
    'MM':'Material and Metallurgical Engineering'
}
programme = {
    '01':'Bachelor of Technology',
    '11':'Master of Technology',
    '12':'Master of Science',
    '21':'Doctor of Philosophy'
}


def name_roll():
    with open('./input/names-roll.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
        for data in reader:
            roll[data[0]]=data[1]

def sub_code():
    with open('./input/subjects-master.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
        for data in reader:
            subject[data[0]]=data

def para_producer(description,answer):
    return Paragraph("<b>"+description+": </b>"+answer,ParagraphStyle('normal',fontName = "Helvetica", fontSize=7.5,alignment=TA_LEFT))

def sem_para_producer(description):
    return Paragraph(description,ParagraphStyle('normal',leading=6.5,fontName = "Helvetica", fontSize=6.5,alignment=TA_CENTER))

def remaining(rollno):
    name_roll()
    sub_code()
    pdf = canvas.Canvas("./transcriptIITP/"+rollno+".pdf",pagesize=landscape(A4))
    
    student = {
        '0':{
            'info':[],
            'spi':0,
            'credits':0,
            'cpi':0
        },
        '1': {
            'info':[],
            'spi':0,
            'credits':0,
            'cpi':0
        },
        '2': {
            'info':[],
            'spi':0,
            'credits':0,
            'cpi':0
        },
        '3': {
            'info':[],
            'spi':0,
            'credits':0,
            'cpi':0
        },
        '4': {
            'info':[],
            'spi':0,
            'credits':0,
            'cpi':0
        },
        '5': {
            'info':[],
            'spi':0,
            'credits':0,
            'cpi':0
        },
        '6': {
            'info':[],
            'spi':0,
            'credits':0,
            'cpi':0
        },
        '7': {
            'info':[],
            'spi':0,
            'credits':0,
            'cpi':0
        },
        '8': {
            'info':[],
            'spi':0,
            'credits':0,
            'cpi':0
        },
        '9': {
            'info':[],
            'spi':0,
            'credits':0,
            'cpi':0
        },
        '10': {
            'info':[],
            'spi':0,
            'credits':0,
            'cpi':0
        },
    }

    with open('./input/grades.csv', 'r') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
        for data in reader1:
            if(data[0]==rollno):
                student[data[1]]['info'].append([data[2],subject[data[2]][1],subject[data[2]][2],data[3],data[4]])
    flow_obj = []
    styles = getSampleStyleSheet() 

    text = []
    logo = []
    para = Paragraph("<u>INTERIM TRANSCRIPT</u>",ParagraphStyle('normal',fontName = "Helvetica-Bold", fontSize=8,alignment=TA_CENTER))
    text.append(para)
    logo.append(Image('./iitp.jpg',100,76))

    frame_left = Frame(12,483, 114,100,showBoundary=1) 
    frame_left.addFromList(logo, pdf) 
    frame_left.addFromList(text, pdf) 


    frame_middle = Frame(126,483, 590,100,showBoundary=1)
    logo = []
    logo.append(Image('./middle.jpeg',560,88))
    frame_middle.addFromList(logo, pdf) 

    text = []
    logo = []
    para = Paragraph("<u>INTERIM TRANSCRIPT</u>",ParagraphStyle('normal',fontName = "Helvetica-Bold", fontSize=8,alignment=TA_CENTER))
    text.append(para)
    logo.append(Image('./iitp.jpg',100,76))
    frame_right = Frame(716,483, 114,100,showBoundary=1) 
    frame_right.addFromList(logo, pdf)
    frame_right.addFromList(text, pdf)

    intro_frame = Frame(193,445, 456,28,showBoundary=1, bottomPadding=0) 
    data4 = [[para_producer("Roll No",rollno),para_producer("Name",roll[rollno]),para_producer("Year of Admission","20"+rollno[0]+rollno[1])],[para_producer("Programme",programme[rollno[2]+rollno[3]]),para_producer("Course",course[rollno[4]+rollno[5]]),]]
    introStyle = TableStyle([("SPAN",(1,1),(2,1))])
    t = Table(data4, colWidths=[150,150,150], rowHeights=[9,9],vAlign="MIDDLE")
    t.setStyle(introStyle)

    text=[TopPadder(t)]
    intro_frame.addFromList(text, pdf) 

    body_frame = Frame(12,12,818,471,showBoundary=1) 
    body_frame.addFromList(flow_obj, pdf) 

    sem_table_frame = Frame(12,12,818,433,bottomPadding=0) 
    ts=TableStyle([("GRID",(0,0),(-1,-1),0.5,colors.black),
                    ("LEFTPADDING",(0,0),(-1,-1),0),
                    ("RIGHTPADDING",(0,0),(-1,-1),0),
                    ("TOPPADDING",(0,0),(-1,-1),0),
                    ("BOTTOMPADDING",(0,0),(-1,-1),1.25),
                    ('VALIGN',(0,0),(-1,-1),'MIDDLE')
                    ])
    crts = TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),
                    ("RIGHTPADDING",(0,0),(-1,-1),0),
                    ("TOPPADDING",(0,0),(-1,-1),0),
                    ("BOTTOMPADDING",(0,0),(-1,-1),1.25),
                    ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                    ('BOX', (0,0), (-1,-1), 0.5, colors.black)
                    ])
    us=TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                    ("LEFTPADDING",(0,0),(-1,-1),7),
                    ("RIGHTPADDING",(0,0),(-1,-1),0),
                    ("TOPPADDING",(0,0),(-1,-1),0),
                    ('LINEBELOW', (0,0), (-1,-1), 0.25, colors.black)
                    ])

    tableToBeInserted = []
    tempTable = []
    for index in range(1,10):
        sem = str(index)
        if(len(student[sem]['info'])):
            data3 = [[sem_para_producer("<b>Sub Code</b>"),sem_para_producer("<b>Subject Name</b>"),sem_para_producer("<b>L-T-P</b>"),sem_para_producer("<b>CRD</b>"),sem_para_producer("<b>GRD</b>")]]
            credit_cleared=0
            prod = 0
            credit_taken=0
            for sub in student[str(index)]['info']:
                data3.append([sem_para_producer(sub[0]),sem_para_producer(sub[1]),sem_para_producer(sub[2]),sem_para_producer(sub[3]),sem_para_producer(sub[4])])
                prod += int(sub[3])*cred[sub[4]]
                credit_taken += int(sub[3])
                if(cred[sub[4]]>=5):
                    credit_cleared += int(sub[3])
            student[sem]['spi'] = ((prod*100)//credit_taken)/100
            student[sem]['credits'] = credit_taken
            numr = 0
            denomr = 0
            for index in range(1,index+1):
                numr += student[str(index)]['spi']*student[str(index)]['credits']
                denomr += student[str(index)]['credits']
            student[sem]['cpi'] = ((numr*100)//denomr)/100


            t = Table(data3, colWidths=[35,150,25,21,21], rowHeights=9)
            t.setStyle(ts)
            para1 = Paragraph("<b><u>Semester "+sem+"</u></b>",ParagraphStyle('normal',leading=8,fontName = "Helvetica-Bold", fontSize=6,alignment=TA_LEFT))
            crt = [[sem_para_producer("Credits Taken: "+str(credit_taken)),sem_para_producer("Credits Cleared: "+str(credit_cleared)),sem_para_producer("SPI: "+str(student[sem]['spi'])),sem_para_producer(" CPI: "+str(student[sem]['cpi']))]]
            # para = Paragraph("Credits Taken: "+str(credit_taken)+"Credits Cleared: "+str(credit_cleared)+" &emsp; SPI: "+str(student[sem]['spi'])+" &emsp; CPI: "+str(student[sem]['cpi']),ParagraphStyle('normal',spaceAbove=2,rightIndent=70,leading=6,borderWidth=0.5,borderPadding=[2,2],borderColor = "black",fontName = "Helvetica",fontSize=6, alignment=TA_CENTER))
            para = Table(crt, colWidths=[65,70,40,40])
            para.setStyle(crts)
            semTable = [Spacer(1,7),para1,Spacer(1,4),t,Spacer(1,10),para,Spacer(1,7)]
            tempTable.append(semTable)
            if(index%3==0):
                tableToBeInserted.append(tempTable)
                tempTable = []
    if(len(tempTable)):
        tableToBeInserted.append(tempTable)
        tempTable = []


    u=Table(tableToBeInserted, colWidths=818/3)
    u.setStyle(us)
    text = [u]
    sem_table_frame.addFromList(text, pdf) 

    frame_date = Frame(24,17,250,15,bottomPadding=0, topPadding=0)
    date_today = str(datetime.now()).split(" ")[0].split('-')
    time_today = str(datetime.now()).split(" ")[1].split(':')
    time_now = date_today[2]+" "+months[date_today[1]]+" "+date_today[0]+", "+time_today[0]+":"+time_today[1]
    para = Paragraph("Date generated : <b>"+time_now+"</b>",ParagraphStyle('normal',leading=8,fontName = "Helvetica-Bold", fontSize=6.5,alignment=TA_LEFT))
    text = [para]
    frame_date.addFromList(text,pdf)

    frame_mohar = Frame(371,24,100,70,bottomPadding=0)
    mohar = []
    if(sys.argv[3]=='true'):
        mohar.append(Image('./input/mohar.jpg',80,60))
    frame_mohar.addFromList(mohar,pdf)

    logo = []
    if(sys.argv[2]=='true'):
        logo.append(Image('./input/signature.jpg',100,30))
    frame_sign = Frame(672,36, 150,40,bottomPadding=0) 
    frame_sign.addFromList(logo, pdf)

    signature_text_frame = Frame(672,17,150,15,bottomPadding=0,topPadding=0)
    text = []
    para = Paragraph("Assistant Registrar (Academic)",ParagraphStyle('normal',fontName = "Helvetica-Bold", fontSize=6.5,alignment=TA_CENTER))
    text.append(para)
    signature_text_frame.addFromList(text, pdf)

    pdf.line(697,34,796,34)
    pdf.line(82,22,142,22)

    pdf.save()

if(sys.argv[1]=="All"):
    with open('./input/names-roll.csv') as csvFile:
        reader = csv.reader(csvFile, delimiter=',', skipinitialspace=True)
        for data in reader:
            if(data[0]=="Roll"):
                continue
            if(data[0][2:4]!='01'):
                remaining(data[0])
else:
    remaining(sys.argv[1])