#!/usr/bin/python
# dont forget to add in setup.py XD
# ros2 pkg create --dependencies rclpy turtlesim --build-type ament_python -- learn_ros
# colcon build
# source install/setup.bash
# ros2 run learn_ros add_service

#Second terminal:
# ros2 service call /add_ints example_interfaces/srv/AddTwoInts "a: 100
# b: 50"  

import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


class AddInts(Node):
    def __init__(self):
        super().__init__('addints')  # Node's name
        print("Init")
        self._service = self.create_service(
            AddTwoInts, 'add_ints', self.addInts)

    def addInts(self, req:AddTwoInts.Request, res:AddTwoInts.Response):
        res.sum=req.a+req.b
        print(f"{req.a} + {req.b} = {res.sum}")
        return res


def main():
    rclpy.init()
    node = AddInts()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
