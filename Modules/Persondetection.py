import cv2
import imutils
import numpy as np
protopath = "Models/MobileNetSSD_deploy.prototxt"
modelpath = "Models/MobileNetSSD_deploy.caffemodel"


def person_detect(image):
    detector = cv2.dnn.readNetFromCaffe(
        prototxt=protopath, caffeModel=modelpath)

    image = imutils.resize(image, width=600)

    (H, W) = image.shape[:2]

    blob = cv2.dnn.blobFromImage(image, 0.007843, (W, H), 127.5)

    detector.setInput(blob)
    person_detections = detector.forward()
    persons = []
    for i in np.arange(0, person_detections.shape[2]):
        confidence = person_detections[0, 0, i, 2]
        if confidence > 0.3:
            person_box = person_detections[0, 0,
                                           i, 3:7] * np.array([W, H, W, H])
            (startX, startY, endX, endY) = person_box.astype("int")
            persons.append(person_box)
            cv2.rectangle(image, (startX, startY),
                          (endX, endY), (0, 0, 255), 2)

    print(' ', len(persons))

    cv2.putText(
        image,
        f'Ilosc osob: {len(persons)}',
        (20,
         50),
        cv2.FONT_HERSHEY_DUPLEX,
        1.5,
        (211, 211, 240), 2)
    cv2.imshow("Results", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
