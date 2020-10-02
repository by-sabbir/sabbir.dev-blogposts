import cv2
import dlib

# loading the haar cascade classifier from XML file
detector = dlib.cnn_face_detection_model_v1('../models/mmod_human_face_detector.dat')

# loading image
img = cv2.imread('../data/face_detection_example.JPG')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
faces = detector(rgb, 0)
print(len(faces))
for face in faces:
    conf = str(face.confidence)
    face = face.rect
    x1, y1 = face.tl_corner().x, face.tl_corner().y
    x2, y2 = face.br_corner().x, face.br_corner().y
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
    cv2.putText(img, conf, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, .3, (0, 255, 0), 1)
# displaying the image and cleaning up
cv2.imshow(f'face detected: {len(faces)}',img)
cv2.waitKey(0)
cv2.destroyAllWindows()