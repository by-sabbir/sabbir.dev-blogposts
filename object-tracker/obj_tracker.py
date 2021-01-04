import cv2
import sys


def main():
    # trackers covered in this scope-
    # KCF, MIL, TLD, CSRT
    cap =  cv2.VideoCapture("/home/alpha/Videos/rocket-launch-STS 125 Mission Highlights.m4v")
    tracker_name = "KCF"

    tracker = cv2.Tracker(tracker_name)

    while True:
        pass



if __name__ == "__main__":
    main()