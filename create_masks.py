import csv
import numpy as np
import cv2

with open('AOI_2_Vegas_Roads_Train.csv') as csvfile:
    truthreader = csv.reader(csvfile, delimiter=',')
    image_name = "delete"
    line = ""
    img = np.zeros((1300,1300,1), np.uint8)

    for row in truthreader:
        if row[0] == image_name:
            line = row[1].replace('LINESTRING (', '').replace(')', '').replace(',', '')
            x = line.split()
            for idx in range((int((len(x)/2))) - 1):
                cv2.line(img, (int(float(x[idx * 2])), int(float(x[idx * 2 + 1]))), (int(float(x[idx * 2 + 2])), int(float(x[idx * 2 + 3]))), (255), 10)

        else:
            cv2.imwrite(image_name + '_mask.png', img)
            #cv2.imshow('image',img)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            img = np.zeros((1300,1300,1), np.uint8)
            image_name = row[0]
            line = row[1].replace('LINESTRING (', '').replace(')', '').replace(',', '')
            x = line.split()
            for idx in range((int((len(x)/2))) - 1):
                cv2.line(img, (int(float(x[idx * 2])), int(float(x[idx * 2 + 1]))), (int(float(x[idx * 2 + 2])), int(float(x[idx * 2 + 3]))), (255), 10)



