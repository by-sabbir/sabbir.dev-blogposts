import cv2
import mtcnn
import tensorflow as tf

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)

cap = cv2.VideoCapture()
detector = mtcnn.MTCNN()

while True:
    _, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = detector.detect_faces(rgb)
    for face in faces:
        x, y, w, h = face.get('box')
        conf = str(face['confidence'])[:4]

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        cv2.putText(frame, conf, (x, y - 7), cv2.FONT_HERSHEY_SIMPLEX, .3, (0, 255, 0), 1)

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
