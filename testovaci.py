import sys
import base64
import time
import subprocess
import os

file_loc_name = "/var/www/html/Timak/facenet/datasets/unknown/raw/rec_this_face.jpg"
raw_dir = "/var/www/html/Timak/facenet/datasets/unknown/raw"
pre_dir = "/var/www/html/Timak/facenet/datasets/unknown/unknown_160"



# Premenna 'string' je string fotografie v base64
string = "" 
for word in sys.argv[1:]:
    string += word + " "

# Overenie ci je string v spravnom formate aby sa vedel v pripade ulozit ako obrazok
imgdata = base64.b64decode(string)
filename = file_loc_name

with open(filename, 'wb') as f:
    f.write(imgdata)

# Simulovanie oneskorenia
# time.sleep(5)

#clean directories
os.system("rm -rf "+ pre_dir)

#preprocesing
os.system("python3 /var/www/html/Timak/facenet/src/align/align_dataset_mtcnn.py "+raw_dir+" "+pre_dir+" --image_size 160 >> /dev/null")

#identifikacia
command = "python3 /var/www/html/Timak/facenet/evaluate.py "+pre_dir+"/rec_this_face.jpg"
#name = subprocess.check_output(command, shell=True).decode('utf-8')
os.system(command)

# Vypis ... toto sa posiela cez php priamo do android aplikacie
#print(name)
