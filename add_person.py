import sys
import subprocess
import os
import shutil
import time

# get name of person
name = sys.argv[1]

# instead of removing and adding new dataset, we just add one person and then retrain
# we need different way of telling if neural network is already training

# delete old dataset
os.chdir('/var/www/html/Timak/facenet/datasets')
shutil.rmtree('live_dataset', ignore_errors=True)

# make new dataset and copy picture
directory = 'live_dataset'
os.makedirs(directory+'/raw/'+name)
os.makedirs(directory+'/'+directory+'_160/'+name)
subprocess.run(['cp', '/var/www/html/Timak/some_image.jpg',
                '/var/www/html/Timak/facenet/datasets/'+directory+'/raw/'+name+'/'])

# ---CNN---
# align picture

subprocess.run(['python3', '/var/www/html/Timak/facenet/src/align/align_dataset_mtcnn.py',
                '/var/www/html/Timak/facenet/datasets/'+directory+'/raw',
                '/var/www/html/Timak/facenet/datasets/'+directory+'/'+directory+'_160',
                '--image_size', '160', '--margin', '32', '--random_order'])

# ---TO DO---
# retrain neural network
