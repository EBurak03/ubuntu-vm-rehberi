#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
import sys
import tty
import termios

class SimpleDroneController:
    def __init__(self):
        rospy.init_node('simple_drone_controller', anonymous=True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        
        self.linear_speed = 0.5
        self.angular_speed = 0.5
        
        rospy.loginfo("=" * 50)
        rospy.loginfo("DRONE KLAVYE KONTROLU HAZIR!")
        rospy.loginfo("=" * 50)
        rospy.loginfo("ONEMLI: Motorlari aktif etmek icin baska bir terminalde su komutu calistir:")
        rospy.loginfo("  rosservice call /enable_motors \"enable: true\"")
        rospy.loginfo("")
        rospy.loginfo("Kontrol Tuslari:")
        rospy.loginfo("  w/x : Yukari/Asagi")
        rospy.loginfo("  i/k : Ileri/Geri")
        rospy.loginfo("  j/l : Sola/Saga")
        rospy.loginfo("  a/d : Sola Don/Saga Don")
        rospy.loginfo("  s   : Dur")
        rospy.loginfo("  q   : Cikis")
        rospy.loginfo("=" * 50)
    
    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key
    
    def run(self):
        twist = Twist()
        
        while not rospy.is_shutdown():
            key = self.get_key()
            
            twist.linear.x = 0
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.z = 0
            
            if key == 'w':
                twist.linear.z = self.linear_speed
                rospy.loginfo("Yukseliyor...")
            elif key == 'x':
                twist.linear.z = -self.linear_speed
                rospy.loginfo("Alcaliyor...")
            elif key == 'i':
                twist.linear.x = self.linear_speed
                rospy.loginfo("Ileri...")
            elif key == 'k':
                twist.linear.x = -self.linear_speed
                rospy.loginfo("Geri...")
            elif key == 'j':
                twist.linear.y = self.linear_speed
                rospy.loginfo("Sola kayiyor...")
            elif key == 'l':
                twist.linear.y = -self.linear_speed
                rospy.loginfo("Saga kayiyor...")
            elif key == 'a':
                twist.angular.z = self.angular_speed
                rospy.loginfo("Sola donuyor...")
            elif key == 'd':
                twist.angular.z = -self.angular_speed
                rospy.loginfo("Saga donuyor...")
            elif key == 's':
                rospy.loginfo("DURDU!")
            elif key == 'q':
                rospy.loginfo("Cikiliyor...")
                break
            else:
                continue
            
            self.pub.publish(twist)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        controller = SimpleDroneController()
        controller.run()
    except rospy.ROSInterruptException:
        pass
