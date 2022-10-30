#!/usr/bin/python
#this is incomplete program

#ros2 pkg create --dependencies rclpy turtlesim --build-type ament_python -- learn_ros
# colcon build
# source install/setup.bash
# ros2 run learn_ros draw_square

#Second terminal:
#ros2 topic echo /gossip
#this is to subscribe to the topic

import rclpy
from rclpy.node import Node
import random

from std_msgs.msg import String

class DrawSquare(Node):
    def __init__(self):
        super().__init__('draw_square')
        print("Init")
        self._topic_pub = self.create_publisher(String,'gossip',10,)
        self._pub_timer = self.create_timer(1,self.draw)

    def draw(self):
        msg = String()
        msg.data = f"Body soda here {random.randint(0,100)}"
        self._topic_pub.publish(msg)

def main():
    rclpy.init()
    node = DrawSquare()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
