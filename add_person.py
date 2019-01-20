import subprocess
import os
import sys
# import time
import warnings
import datetime

# get name of person
# maybe also surname?
name = sys.argv[1]
warnings.filterwarnings("ignore")
# we need different way of telling if neural network is already training

# delete old dataset
os.chdir('/var/www/html/Timak/facenet/datasets')
# shutil.rmtree('live_dataset', ignore_errors=True)
img_name = str(datetime.datetime.now())

# make new dataset and copy picture
try:
    os.makedirs('live_dataset/raw/' + name)
except OSError as e:
    # directory exists
    print('Person exists')

os.makedirs('live_dataset/live_dataset_160/'+name)
subprocess.run(['cp', '/var/www/html/Timak/some_image.jpg',
                '/var/www/html/Timak/facenet/datasets/live_dataset/raw/'+name+'/'+img_name])
