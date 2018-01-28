a = ["0.00 71.52 8.99 71.46 0.00 329.52 1.79 329.55 8.99 71.46 7.96 108.40 2.62 299.86 1.79 329.55 0.00 393.47 833.43 308.34 554.19 303.07 335.26 302.02 2.62 299.86 837.48 118.01 530.92 115.88 171.34 106.36 7.96 108.40 8.99 71.46 10.81 0.00 224.74 976.76 326.27 978.88 476.45 955.61 611.83 936.57 818.49 938.77 837.48 118.01 834.98 242.79 833.43 308.34 818.49 938.77 817.22 992.64 809.93 1300.00 817.22 992.64 1300.00 992.27 837.48 118.01 839.54 0.00 1300.00 316.77 1296.62 316.82"]

x = a[0].split()

y = [2.00, 450.22, 900.99, 65.22]

import numpy as np
import cv2

# Create a black image
img = np.zeros((1300,1300,1), np.uint8)
image_name = "hello.png"

print(len(x)/4)
# Draw a diagonal blue line with thickness of 5 px
#it = iter(x)
print((int((len(x)/2))) - 1)

for idx in range((int((len(x)/4))) - 1):
    cv2.line(img, (int(float(x[idx * 4])), int(float(x[idx * 4 + 1]))), (int(float(x[idx * 4 + 2])), int(float(x[idx * 4 + 3]))), (255), 5)
#    cv2.line(img, ((int(float(x[idx * 4)]), (int(float(x[idx * 4 + 1)])), ((int(float(x[idx * 4 + 2)]), (int(float(x[idx * 4 + 3)])),(255),5)

#cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(image_name, img)
