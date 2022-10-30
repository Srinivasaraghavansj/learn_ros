#!/usr/bin/python

#ros2 pkg create --dependencies rclpy turtlesim --build-type ament_python -- learn_ros
# colcon build
# source install/setup.bash
# ros2 run learn_ros listener

#Second terminal:
#ros2 topic echo /me_talks
#this is to subscribe to the topic

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Listen(Node):
    def __init__(self):
        super().__init__('listen')
        print("Init")
        self._topic_sub = self.create_subscription(String,'me_talks',self.listen,10)

    def listen(self,msg):
        print(msg.data)

def main():
    rclpy.init()
    node = Listen()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
