#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------
#Title: ゴミをゴミ箱まで運ぶプログラム
#Author: Koya Okuse
#Data: 2021/08/24
#Memo:WRS大会用プログラム
#-------------------------------------------------------------------
import time
import sys

import rospy
from std_msgs.msg import String
import smach
import smach_ros

import Levenshtein

sys.path.insert(0, '/home/athome/catkin_ws/src/mimi_common_pkg/scripts')
from common_action_client import *
from common_function import *
from mimi_common_pkg.srv import ManipulateSrv, RecognizeCount
from voice_common_pkg import SpeechToText

def main():
    stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)
    pub_location = rospy.Publisher('/navigation/move_place', String, queue_size = 1)

    count = 0
    #EnterRoom
    enterTheRoomAC(0.8)

    print "start Q and A session"
    speak("start Q and A session")
    #voice_recognition
    while 1:
        speak("Please ask me a question.")
        result = self.stt_pub(str_short=False,
                                    context_phrases=[phrases_list],boost_value=20.0)

        


    #Exit_Room
    speak('Go to the exit')
    location_list = searchLocationName('entrance')
    navigationAC(location_list)
    speak('finish 24 challenge 2')
