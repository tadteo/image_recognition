#!/usr/local/bin/python3
import numpy as np
import cv2
import os
# Open image and make into numpy array
images = []
THRESHOLD = 150
for i in range(10,23):
    # im = cv2.imread('./imgs/20201012_180710'+str(i)+'_R.jpg')
    im = cv2.imread(os.environ['HOME']+'/Thermal/20201012_180710/20201012_1807'+str(i)+'_R.jpg')
    print(im)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    images.append(gray)

for index,i in enumerate(images):
    cv2.imshow('Original image',i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ret, thresh = cv2.threshold(i,THRESHOLD,255,0)
    contours , hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(i,contours,-1, (0,255,0,3))
    for idx,raw in enumerate(i):
        for idx2,column in enumerate(raw):
            if( column >= THRESHOLD):
                print("Found something")
                print("Pixel", idx, idx2, "intensity", column)
                i[idx,idx2]=255
    cv2.imshow('Original image',i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # print(i[250,320])
    # print(i[250, 320] >= 120)
# gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)



print(im.shape)
# Work out what we are looking for
sought = [254,254,254]

# for i in im:
#     for j in i:
#         for k in j:
#             print("color",k)
        

result = np.count_nonzero(np.all(im==sought,axis=2))
print(result)