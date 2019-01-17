import subprocess
import os
# import shutil
import socket
import sys
import time
import warnings

# get name of person
# maybe also surname?
name = sys.argv[1]
warnings.filterwarnings("ignore")
# we need different way of telling if neural network is already training

# delete old dataset
os.chdir('/var/www/html/Timak/facenet/datasets')
# shutil.rmtree('live_dataset', ignore_errors=True)

# make new dataset and copy picture
try:
    os.makedirs('live_dataset/raw/' + name)
except OSError as e:
    # directory exists
    print("Person already exists")

os.makedirs('live_dataset/live_dataset_160/'+name)
subprocess.run(['cp', '/var/www/html/Timak/some_image.jpg',
                '/var/www/html/Timak/facenet/datasets/live_dataset/raw/'+name+'/'])

# ---CNN---
# align picture

subprocess.run(['python3', '/var/www/html/Timak/facenet/src/align/align_dataset_mtcnn.py',
                '/var/www/html/Timak/facenet/datasets/live_dataset/raw',
                '/var/www/html/Timak/facenet/datasets/live_dataset/live_dataset_160',
                '--image_size', '160', '--margin', '32', '--random_order'])

# retrain neural network
subprocess.run(['python3', '/var/www/html/Timak/facenet/src/classifier.py', 'TRAIN',
                '/var/www/html/Timak/facenet/datasets/live_dataset/live_dataset_160/',
                '/var/www/html/Timak/facenet/models/20180402-114759/20180402-114759.pb',
                '/var/www/html/Timak/facenet/models/20180402-114759/my_classifier.pkl', '--batch_size', '1000'])

# ---TO DO---
# signal end of traning somehow
print('All done motherfuckers!!!')
