#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import glob
import argparse
import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help='images folder', required=True)
    parser.add_argument('-f', help='frame rate', required=True)
    parser.add_argument('-d', help='Debug option', required=None)
    
    args = parser.parse_args()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, float(args.f), (384,288))
 
    input_fnames = glob.glob(args.p+"/*.jpg")
    input_fnames = np.sort(input_fnames)

    for fname in input_fnames:
        frame = cv2.imread(fname)

        out.write(frame)

        if args.d:
            cv2.imshow("frame", frame)

        k = cv2.waitKey(1) & 0xff
        if(k == 27):
            break

    out.release()
    cv2.destroyAllWindows()
