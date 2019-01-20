import subprocess
import os
import sys
import warnings
import datetime

# get name of person
# maybe also surname?
name = sys.argv[1]
warnings.filterwarnings("ignore")

os.chdir('/var/www/html/Timak/facenet/datasets')
img_name = str(datetime.datetime.now())
dir_exists = False

# make new dataset and copy picture
try:
    os.makedirs('live_dataset/raw/' + name)
except OSError as e:
    # directory exists
    print('Adding to existing dir')
    dir_exists = True

if dir_exists is False:
    os.makedirs('live_dataset/live_dataset_160/'+name)

output = subprocess.check_output(['cp', '/var/www/html/Timak/some_image.jpg',
                                  '/var/www/html/Timak/facenet/datasets/live_dataset/raw/'+name+'/'+img_name+'.jpg'])

print(output.decode("utf-8"))
