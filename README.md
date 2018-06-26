# image_to_video
Python script to convert images into video frames with OpenCV

## dependencies

* OpenCV 3+
* glob
* argparse
* numpy

## hot to use
```
$ python image_to_video.py -p ./D1_cam_1/ -f 24
$ python image_to_video.py -h
usage: image_to_video.py [-h] -p P -f F [-d D]

optional arguments:
  -h, --help  show this help message and exit
  -p P        images folder
  -f F        frame rate
  -d D        Debug option

```
Where D1_cam_1 is the folder that contains the images
