#!/usr/local/bin/python3
import numpy as np
import cv2
import os 


THRESHOLD = 150


if __name__ == "__main__":

    #open video
    cap = cv2.VideoCapture(os.environ['HOME']+'/Thermal/20201006_183919/file:///home/matteo/Thermal/night_1/20201025_155119_H264_A.mov')


    i=0

    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Define the codec and create VideoWriter object
    print("open fourccc")
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    print("videowriter...")
    out = cv2.VideoWriter('./output.avi',fourcc, 20.0, (frame_width,frame_height),0)

    while(cap.isOpened()):
        i+=1
        print("Working on frame: " , i, end='\r')
        ret,frame = cap.read()
        # print(frame.shape)
        # print(ret)
        if(ret==False):
            print()
            break
        

        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(frame,THRESHOLD,255,0)
        contours , hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            # print("x: {}, y: {}, w: {}, h: {} ".format(x,y,w,h))
            rect = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            # print(type(rect))
            # rect = np.int0(rect)
            # print('\n',rect.shape)
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            # print("\n Box shape: ",box.shape)
            cv2.drawContours(frame,[box],0,(0,0,255),2)
            # cv2.drawContours(frame,[rect],0, (0,0,255,2))

        cv2.drawContours(frame,contours,-1, (0,255,0,3))

        out.write(frame)

        cv2.imshow('frame',frame)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     print("Video closed by user")
        #     break
    cap.release()
    out.release
    cv2.destroyAllWindows()  
    print("END")