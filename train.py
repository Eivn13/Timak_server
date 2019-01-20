import subprocess

# ---CNN---
# align picture

subprocess.run(['python3', '/var/www/html/Timak/facenet/src/align_dataset_mtcnn.py',
                '/var/www/html/Timak/facenet/datasets/live_dataset/raw',
                '/var/www/html/Timak/facenet/datasets/live_dataset/live_dataset_160',
                '--image_size', '160', '--margin', '32', '--random_order'])

# retrain neural network
subprocess.run(['python3', '/var/www/html/Timak/facenet/src/classifier.py', 'TRAIN',
                '/var/www/html/Timak/facenet/datasets/live_dataset/live_dataset_160/',
                '/var/www/html/Timak/facenet/models/20180402-114759/20180402-114759.pb',
                '/var/www/html/Timak/facenet/models/20180402-114759/my_classifier.pkl', '--batch_size', '1000'])

# signal end of traning somehow
print('Training is done.')
