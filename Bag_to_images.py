
import os
import argparse

import sys
sys.path.remove('/opt/ros/melodic/lib/python2.7/dist-packages') # in order to import cv2 under python3
import cv2
sys.path.append('/opt/ros/melodic/lib/python2.7/dist-packages') # append back in order to import rospy

import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bag_file = "/home/imad/Downloads/KITTI.bag" # path to bag files
outpu_dir = "/home/imad/Downloads/saved_images" # path to saved images
image_topic = "/kitti/camera_color_left/image_raw" # topic


    #print "Extract images from %s on topic %s into %s" % (args.bag_file,args.image_topic, args.output_dir)
bag = rosbag.Bag(bag_file, "r")
bridge = CvBridge()
count = 0
for topic, msg, t in bag.read_messages(topics=[image_topic]):
    cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")

    cv2.imwrite(os.path.join(outpu_dir, "frame%06i.png" % count), cv_img)
        #print "Wrote image %i" % count

    count += 1
