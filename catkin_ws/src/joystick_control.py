#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoystickDrone:
    def __init__(self):
        rospy.init_node('joystick_drone_controller')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/joy', Joy, self.joy_callback)
        rospy.loginfo("Joystick Kontrolu Basladi!")

    def joy_callback(self, data):
        twist = Twist()
        # Eksen eslestirmeleri (Joystick modeline gore degisebilir)
        # Sol Analog: Ileri/Geri (axes[1]), Sag/Sol (axes[0])
        # Sag Analog: Yukari/Asagi (axes[4]), Donme (axes[3])
        twist.linear.x = data.axes[1] * 2.0
        twist.linear.y = data.axes[0] * 2.0
        twist.linear.z = data.axes[4] * 2.0
        twist.angular.z = data.axes[3] * 2.0
        self.pub.publish(twist)

if __name__ == '__main__':
    try:
        JoystickDrone()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
