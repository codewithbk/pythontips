import os 
import shutil
import time

files = os.listdir()
path = os.getcwd()
print("\n Hey These is auto seperate the file and also detele those folder are completly empty so you run carefully !")

music = ['.mp3','.wav', '.aac', '.ogg','.aif',]
coding = ['.java','.html','.cpp','.css','.js','.jsp','.asp','.php','.xhtml','.class', '.h','.swift',]
compressed_file = ['.zip','.rar','.pkg','.rpm','.tar.gz', '.z',]
log_file = ['.log','.xml','.sav', '.dat',]
data_base = ['.dbf', '.db', '.sql',]
ms_office = ['.ods','.xls','.xlsm','.xlsx','.cab','.cur','cur','.odt']
window_file = ['.bat','mdb',]
video = ['.mp4','.mov','.mov','.mkv',]
pdf_file = ['.pdf','.doc','.docx']
txt = ['.txt','.text','.tex']
software = ['.exe','.msi']
hidden = ['',]
image = ['.jpg','.jpeg','.png',]
total = []

# if you add more tool you make list like this # check what folder i create it already exists or not.

def iffolderis(folder):
  if not os.path.exists(folder):
    os.mkdir(folder)
    time.sleep(1)
    print(f'"{folder}" folder created!')
  elif os.path.exists(folder):
    print(f"\nOperation fail because '{folder}' folder is already exists You delete those other wise change code : ")


def movefile(path, anotherpath):
   shutil.move(path, anotherpath)

def totalmake(files, choice, folder):
  iffolderis(folder)
  for files in files:
    if os.path.splitext(files)[1].lower() in choice:
      total = path + '/' + files
      total2 = path + '/' + folder + '/' + files  
      movefile(total, total2)
      print(f'Done "{files}" file move in "{folder}" folder')

totalmake(files, image, 'Image file')
totalmake(files, hidden, 'Hidden file')
totalmake(files, software, 'Software')
totalmake(files, txt, 'Text file')
totalmake(files, pdf_file, 'Pdf file')
totalmake(files, video, 'Video file')
totalmake(files, window_file, 'Windows file')
totalmake(files, ms_office, 'Ms files')
totalmake(files, data_base, 'Database file')
totalmake(files, log_file, 'log file')
totalmake(files, compressed_file, 'Compressed files')
totalmake(files, coding, 'Coding file')
totalmake(files, music, 'Music file')

files = os.listdir()

for i in files:
  if os.path.isdir(i):
    total.append(i)

#print(total)
#print(files)

for i in total:
  if len(os.listdir(i)) == 0:
    directory = i
    parent = os.path.join(path, directory) 
    os.rmdir(parent)
    print(f'Remove unwanted folder "{i}"')

time.sleep(2)
print('Done :)')
