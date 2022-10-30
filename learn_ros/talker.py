#!/usr/bin/python
#dont forget to add in setup.py XD
#ros2 pkg create --dependencies rclpy turtlesim --build-type ament_python -- learn_ros
# colcon build
# source install/setup.bash
# ros2 run learn_ros talker

#Second terminal:
#ros2 topic echo /me_talks
#this is to subscribe to the topic


#Talk using command line:
#ros2 topic pub -1 /me_talks std_msgs/msg/String "data: 'hello ros'"

import rclpy
from rclpy.node import Node
import random

from std_msgs.msg import String

class Talk(Node):
    def __init__(self):
        super().__init__('talker')
        print("Init")
        self._topic_pub = self.create_publisher(String,'me_talks',10,)
        self._pub_timer = self.create_timer(1,self.talk)

    def talk(self):
        msg = String()
        msg.data = f"Body soda here {random.randint(0,100)}"
        self._topic_pub.publish(msg)

def main():
    rclpy.init()
    node = Talk()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
