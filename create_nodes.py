import csv
import numpy as np
import cv2

with open('AOI_5_Khartoum_Roads_Train.csv') as csvfile:
    truthreader = csv.reader(csvfile, delimiter=',')
    image_name = "delete"
    line = ""
    img = np.zeros((1300,1300,1), np.uint8)
    radius = 3

    for row in truthreader:
            if row[0] == image_name:
                line = row[1].replace('LINESTRING (', '').replace(')', '').replace(',', '')
                x = line.split()
                for idx in range((int((len(x)/2))) - 1):
                    xmin = (int(float(x[idx * 2]) - radius))
                    ymin = (int(float(x[idx * 2 + 1]) - radius))
                    xmax = (int(float(x[idx * 2]) + radius))
                    ymax = (int(float(x[idx * 2 + 1]) + radius))

                    if xmin < 0:
                        xmin = 0
                    if ymin < 0:
                        ymin = 0
                    if xmax > 1300:
                        xmax = 1300
                    if ymax > 1300:
                        ymax = 1300
                    
                    pts = np.array([[xmin, ymin], [xmin, ymax], [xmax, ymax], [xmax, ymin]])
                    pts = pts.reshape((-1,1,2))
                    cv2.polylines(img,[pts],True,(255),thickness=radius+2)
                    
            else:
                cv2.imwrite(image_name + '_nodes.png', img)
                #cv2.imshow('image',img)
                #cv2.waitKey(0)
                #cv2.destroyAllWindows()
                img = np.zeros((1300,1300,1), np.uint8)
                image_name = row[0]
                line = row[1].replace('LINESTRING (', '').replace(')', '').replace(',', '')
                x = line.split()
                for idx in range((int((len(x)/2))) - 1):
                    xmin = (int(float(x[idx * 2]) - radius))
                    ymin = (int(float(x[idx * 2 + 1]) - radius))
                    xmax = (int(float(x[idx * 2]) + radius))
                    ymax = (int(float(x[idx * 2 + 1]) + radius))

                    if xmin < 0:
                        xmin = 0
                    if ymin < 0:
                        ymin = 0
                    if xmax > 1300:
                        xmax = 1300
                    if ymax > 1300:
                        ymax = 1300
                    
                    pts = np.array([[xmin, ymin], [xmin, ymax], [xmax, ymax], [xmax, ymin]])
                    pts = pts.reshape((-1,1,2))
                    cv2.polylines(img,[pts],True,(255),thickness=radius+2)

