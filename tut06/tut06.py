import re,shutil,os

# Creating correct_srt folder
try:
  os.mkdir("./correct_srt")
except FileExistsError:
  pass

# Function to add web series to correct_srt folder before procesing
def addFolderToCorrectFolder(name):
    try:
        shutil.copytree('./wrong_srt/'+name,'./correct_srt/'+name)
    except:
        shutil.rmtree('./correct_srt/'+name)
        shutil.copytree('./wrong_srt/'+name,'./correct_srt/'+name)

# Function to add padding to episode and season number
def add_padding(data,padding):
    res=str(data)
    zero = ""
    for i in range(0,padding-len(res)):
        zero+='0'
    res=zero+res
    return res

# Helper function for renaming the files
def helper_function(series_number, season_padding, episode_padding):
    if(series_number==1):
        addFolderToCorrectFolder('Breaking Bad')
        name_compiler = re.compile(r' 720p\.BRrip\.Sujaidr')
        season_compiler = re.compile(r's\d\de\d\d')
        for filename in os.listdir('./correct_srt/Breaking Bad'):
            season = re.findall('\d\d',filename)
            final_saesonname = "Season "+add_padding(int(season[0]),season_padding)+" Episode "+add_padding(int(season[1]),episode_padding)
            file = name_compiler.sub("",filename)
            final_filename = season_compiler.sub(final_saesonname,file)
            os.rename('./correct_srt/Breaking Bad/'+filename,'./correct_srt/Breaking Bad/'+final_filename)
    
    elif(series_number==2):
        addFolderToCorrectFolder('Game of Thrones')
        name_compiler = re.compile(r'.WEB.REPACK.MEMENTO.en')
        season_compiler = re.compile(r'\dx\d\d')
        for filename in os.listdir('./correct_srt/Game of Thrones'):
            season = re.findall('\d\d|\d',filename)
            final_saesonname = "Season "+add_padding(int(season[0]),season_padding)+" Episode "+add_padding(int(season[1]),episode_padding)
            file = name_compiler.sub("",filename)
            final_filename = season_compiler.sub(final_saesonname,file)
            os.rename('./correct_srt/Game of Thrones/'+filename,'./correct_srt/Game of Thrones/'+final_filename)
    
    elif(series_number==3):
        addFolderToCorrectFolder('Lucifer')
        name_compiler = re.compile(r'.HDTV.CAKES.en')
        season_compiler = re.compile(r'\dx\d\d')
        for filename in os.listdir('./correct_srt/Lucifer'):
            season = re.findall('\d\d|\d',filename)
            final_saesonname = "Season "+add_padding(int(season[0]),season_padding)+" Episode "+add_padding(int(season[1]),episode_padding)
            file = name_compiler.sub("",filename)
            final_filename = season_compiler.sub(final_saesonname,file)
            os.rename('./correct_srt/Lucifer/'+filename,'./correct_srt/Lucifer/'+final_filename)

# Main fuction
def regex_renamer():
    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))

    helper_function(webseries_num,season_padding,episode_padding)

# Function call
regex_renamer()