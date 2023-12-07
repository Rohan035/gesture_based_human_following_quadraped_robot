#!/usr/bin/env python3
import rospy
import sys
sys.path.append("/home/jarvis/catkin_ws/src/construction-robotics-ws-2023_24/midog_sim/midog_controller")
from src.nodes.controller import Controller

if __name__ =='__main__':
    miDog = Controller(0.02)
    while not rospy.is_shutdown():
        miDog.set_balance()
        for i in range(5):
            miDog.crawl_forward()
             
