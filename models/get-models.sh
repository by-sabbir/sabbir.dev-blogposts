#!/bin/bash
wget http://dlib.net/files/mmod_human_face_detector.dat.bz2
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
echo "##############################"
echo "Download Completed"
bzip2 -d *.bz2
echo "##############################"
echo "Extraction Completed"
echo "##############################"
echo "Downloading GOTURN"
git clone https://github.com/spmallick/goturn-files.git &&
cat goturn.caffemodel.zip* > goturn.caffemodel.zip &&
unzip goturn.caffemodel.zip

echo "##############################"
echo "Download and Extraction Completed"