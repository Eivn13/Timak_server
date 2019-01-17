import sys
import base64
import time
import subprocess
import os

file_loc_name = "/var/www/html/Timak/facenet/datasets/unknown/raw/Test/rec_this_face.jpg"
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

# ak neprepisuje obrazok
# subprocess.run(['rm', '/var/www/html/Timak/facenet/datasets/unknown/unknown_160/Test/rec_this_face.png'])
print("align\n")
# cnn ALIGN
subprocess.run(['python3', '/var/www/html/Timak/facenet/src/align/align_dataset_mtcnn.py',
                '/var/www/html/Timak/facenet/datasets/unknown/raw/',
                '/var/www/html/Timak/facenet/datasets/unknown/unknown_160/',
                '--image_size', '160', '--margin', '32', '--random_order'])
print("classifying\n")
# classify
output = subprocess.check_output(['python3', '/var/www/html/Timak/facenet/src/classifier.py', 'CLASSIFY',
                '/var/www/html/Timak/facenet/datasets/unknown/unknown_160/',
                '/var/www/html/Timak/facenet/models/20180402-114759/20180402-114759.pb',
                '/var/www/html/Timak/facenet/models/20180402-114759/my_classifier.pkl', '--batch_size', '1000'])

# tento hnus by sa mohol presunut do shellu
output = output.decode("utf-8")
output = output.splitlines()
output = output[-2]
output = output.split()
pretty_output = output[1]
certainity = float(output[2])

print(output[2])
if certainity > 0.5:
    print(pretty_output[:-1])
else:
    print("Unknown")

# Simulovanie oneskorenia
# time.sleep(5)

#clean directories
# comm = "rm "+ pre_dir + "/Test/rec_this_face.png"
# print(comm)
#os.system("rm "+ pre_dir + "/Test/rec_this_face.png")

#preprocesing
#os.system("python3 /var/www/html/Timak/facenet/src/align/align_dataset_mtcnn.py "+raw_dir+" "+pre_dir+" --image_size 160 --margin 32 --random_order")

#identifikacia
#command = "python3 /var/www/html/Timak/facenet/evaluate.py "+pre_dir+"/Test/rec_this_face.png"
# command = "python3 /var/www/html/Timak/facenet/src/classifier.py CLASSIFY /var/www/html/Timak/facenet/datasets/unknown/unknown_160 /var/www/html/Timak/facenet/models/20180402-114759/20180402-114759.pb /var/www/html/Timak/facenet/models/20180402-114759/my_classifier.pkl --batch_size 1000 | tail -2"
#name = subprocess.check_output(command, shell=True).decode('utf-8')
#os.system(command)

# Vypis ... toto sa posiela cez php priamo do android aplikacie
#print(command)
#os.system(command).split(" ")[1]
#print("Koksot")
#print("ze by si tu mohol mat meno snad")
