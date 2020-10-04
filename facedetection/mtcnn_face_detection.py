import cv2
import mtcnn
import tensorflow as tf

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)

# loading image
img = cv2.imread('../data/41235_2018_116_Fig3_HTML.png')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

detector = mtcnn.MTCNN()
faces = detector.detect_faces(rgb)
print(len(faces))
for face in faces:
    x, y, w, h = face.get('box')
    conf = str(face['confidence'])[:4]

    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
    cv2.putText(img, conf, (x, y - 7), cv2.FONT_HERSHEY_SIMPLEX, .3, (0, 255, 0), 1)

cv2.imshow("faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
