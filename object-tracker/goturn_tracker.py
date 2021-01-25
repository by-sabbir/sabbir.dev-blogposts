import cv2



def main(source):
    cap = cv2.VideoCapture(source)
    tracker = cv2.TrackerGOTURN_create()
    bbox = None
    box = None
    msg = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Cannot read from source")

        if bbox is not None:
            msg, box = tracker.update(frame)

        if msg:
            x, y, w, h = [p for p in box]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 200, 31), 1)

        if cv2.waitKey(10) & 0xff == 27:
            break

        if cv2.waitKey(10) & 0xff == ord('t'):
            bbox = cv2.selectROI("GOTURN Tracker", frame, showCrosshair=False, fromCenter=False)
            tracker.init(frame, bbox)

        cv2.imshow("GOTURN Tracker", frame)


if __name__ == "__main__":
    vid_source = "/home/sabbir/Videos/sattelite.m4v"
    main(vid_source)
