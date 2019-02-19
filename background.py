#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright 2019 Enric Moreu. All Rights Reserved.

import os
import cv2
import numpy as np

alpha = 0.001
update_rate = 1 - alpha

if not os.path.exists('/code/backgrounds'):
    os.makedirs('/code/backgrounds')



for root, dirs, files in os.walk('/data/train'):
    for name in files:
        if name.endswith('.mp4'):
            video_url = os.path.join(root,name)
            cap = cv2.VideoCapture(video_url)

            length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            print('total number of frames:', length)

            # read the first frame as the background
            if(cap.isOpened()):
                _, background = cap.read()



            frame_counter = 0
            while(cap.isOpened()):
                
                # Capture frame-by-frame
                ret, frame = cap.read()

                #print(frame.)
                    
                if ret:    
                    # calculate new background:
                    background = background * update_rate + alpha * frame
                
                    
                    
                    #if frame_counter == 2000:
                    #    cv2.imshow('frame',background)
                    #    print(np.max(background))
                    #    cv2.waitKey()
                    #    break
                

                    frame_counter = frame_counter + 1

                    if(frame_counter * 10 % length == 0):
                        print(frame_counter, frame_counter*100//length, '% Done')
                
                else:
                        
                    print("video reach the end")
                    break
                
            # When everything done, release the capture
            cap.release()
            #cv2.destroyAllWindows()
            cv2.imwrite('background_fullvideo_v' + str(name) + '.png',background)