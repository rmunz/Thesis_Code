#!/usr/bin/env python

# This file is made from opt_flow.py in the opencv python samples. Because of
# this, we need to first append the path to the opencv sample directory.
import sys
sys.path.append('/home/ryan/opencv/samples/python2')

import numpy as np
import math
import cv2
import video
import time

help_message = '''
USAGE: opt_flow.py [<video_source>]
'''

def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1)
    fx, fy = flow[y,x].T
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(vis, lines, 0, (0, 255, 0))
    for (x1, y1), (x2, y2) in lines:
        cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
    return vis

def magnitude(pix):
    x = pix[1]
    y = pix[0]
    mag = math.sqrt((x*x) + (y*y))
    return mag

def segment(img, flow):
    threshold = 10
    size = flow.shape
    flowMag = np.zeros((size[0], size[1]))
    for i in range(size[0]):
        for j in range(size[1]):
            flowMag[i][j] = magnitude(flow[i][j])
            if flowMag[i][j] <= threshold:
                img[i][j] = 0
    #TODO: Determine Threshold Magnitude
    return img

if __name__ == '__main__':
    print help_message
    try:
        fn = sys.argv[1]
    except:
        fn = 0

    cam = video.create_capture(fn)
    ret, prev = cam.read()
    prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    cur_glitch = prev.copy()

    while True :
        ret, img = cam.read()
        if ret:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            prevgray = gray

        newGray = segment(gray, flow)
        cv2.imshow('flow', draw_flow(newGray, flow))

        ch = 0xFF & cv2.waitKey(5)
        if ch == 27:
            break
        time.sleep(1)
    cv2.destroyAllWindows()
