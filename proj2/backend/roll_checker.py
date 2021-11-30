import re,sys,os,shutil

try:
    os.mkdir('./transcriptIITP')
except FileExistsError:
    shutil.rmtree('./transcriptIITP')
    os.mkdir('./transcriptIITP')

roll_compiler = re.compile(r'\d\d\d\d[A-Za-z][A-Za-z]\d\d')

startRoll = sys.argv[1]
endRoll = sys.argv[2]

bool1 = bool(re.match(r'\d\d\d\d[A-Za-z][A-Za-z]\d\d$',startRoll))
bool2 = bool(re.match(r'\d\d\d\d[A-Za-z][A-Za-z]\d\d$',endRoll))

if((bool1 and bool2)==False):
    print("False")