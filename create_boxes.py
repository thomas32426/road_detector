import csv
import re
import numpy as np


def get_truths(labels_file):
    truths = []
    
    with open(labels_file) as csvfile:
        truthreader = csv.reader(csvfile, delimiter=',')
        image_name = ""
        line = ""
        entry = []
        
        for row in truthreader:
            if row[0] == image_name:
                line = row[1].replace('LINESTRING (', '').replace(')', '').replace(',', '')
                entry.append(line)
            else:
                s = " "
                truths.append(s.join(entry).split())
                image_name = row[0]
                line = row[1].replace('LINESTRING (', '').replace(')', '').replace(',', '')
                entry = []
                entry.append(line)

    return truths   

def make_boxes(csv_file, box_radius=10):
    boxes = get_truths(csv_file)

    return boxes

box_labels = make_boxes('AOI_2_Vegas_Roads_Train.csv')
print(box_labels[2])

