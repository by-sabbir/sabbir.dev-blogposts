import cv2
# loading the haar cascade classifier from XML file
clf = cv2.CascadeClassifier('../models/haarcascade_frontalface_default.xml')

# loading image
img = cv2.imread('../data/face_detection_example.JPG')
print(img.shape) # image shape (height x width x number of channel)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect and draw rectangle
faces = clf.detectMultiScale(gray,
                             scaleFactor=1.3,
                             minNeighbors=9,)
print(f"total face detected: {len(faces)}")
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x, y),(x + w, y + h), (255, 255, 255), 3)
# displaying the image and cleaning up
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()