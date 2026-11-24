#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_srvs.srv import SetBool

def enable_motors():
    rospy.init_node('enable_motors_node', anonymous=True)
    rospy.loginfo("Motor servisi bekleniyor...")
    rospy.wait_for_service('/enable_motors')
    
    try:
        enable_service = rospy.ServiceProxy('/enable_motors', SetBool)
        response = enable_service(True)
        
        if response.success:
            rospy.loginfo("✅ Motorlar başarıyla aktif edildi!")
        else:
            rospy.logwarn("⚠️ Motorlar aktif edilemedi!")
            
    except rospy.ServiceException as e:
        rospy.logerr(f"❌ Servis hatası: {e}")

if __name__ == '__main__':
    try:
        enable_motors()
    except rospy.ROSInterruptException:
        pass
