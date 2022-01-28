from tkinter import N
import cv2
from Modules.Persondetection import person_detect
import glob


def main():
    cv_img = []
    for img in glob.glob("img/*.jpg"):
        n = cv2.imread(img)
        cv_img.append(n)
        person_detect(n)


if __name__ == "__main__":
    main()
