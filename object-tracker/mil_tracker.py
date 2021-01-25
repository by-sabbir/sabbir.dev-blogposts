import cv2
import sys


def main():
    # trackers covered in this scope-
    # KCF, MIL, TLD, CSRT
    cap =  cv2.VideoCapture("/home/sabbir/Videos/sattelite.m4v")
    tracker = cv2.TrackerMIL_create()
    _, init_frame = cap.read()
    # tracker = cv2.Tracker(tracker_name)
    bbox = None
    msg = None
    box = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Parsing is false")

        if bbox is not None:
            msg, box = tracker.update(frame)
        
        if msg:
            x, y, w, h = [p for p in box]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 200, 3), 1)

        cv2.imshow(f"MIL Tracker", frame)

        if cv2.waitKey(10) & 0xff == 27:
            break
        if cv2.waitKey(10) & 0xff == ord('t'):
            bbox = cv2.selectROI("Select box to track", frame, fromCenter=False,
			showCrosshair=True)
            tracker.init(frame, bbox)
        
    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()