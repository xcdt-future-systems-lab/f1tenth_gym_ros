# import the Empty module from std_servs service interface
from std_srvs.srv import Empty
# import the Twist module from geometry_msgs messages interface
from geometry_msgs.msg import Twist
# import the ROS2 python client libraries
import rclpy
from rclpy.node import Node


class DriveServiceServer(Node):

    def __init__(self):
        # Here we have the class constructor

        # call the class constructor to initialize the node as service_moving
        super().__init__('drive_service_server')
        # create the service server object
        # defines the type, name and callback function
        self.srv = self.create_service(Empty, 'driving', self.Empty_callback)
        # create the publisher object
        # in this case the publisher will publish on /cmd_vel topic with a queue size of 10 messages.
        # use the Twist module
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        

    def Empty_callback(self, request, response):
        # The callback function recives the self class parameter, 
        # received along with two parameters called request and response
        # - receive the data by request
        # - return a result as response

        # create a Twist message
        msg = Twist()
        # define the linear x-axis velocity of /cmd_vel topic paramater to 0.3
        msg.linear.x = 0.3
        # define the angular z-axis velocity of /cmd_vel topic paramater to 0.3
        msg.angular.z = 0.0
        # Publish the message to the topic
        self.publisher_.publish(msg)
        # print a pretty message
        self.get_logger().info('RUN ROBOT RUN!')
        
        
        # return the response parameter
        return response


def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    moving_service = DriveServiceServer()
    # pause the program execution, waits for a request to kill the node (ctrl+c)
    rclpy.spin(moving_service)
    # shutdown the ROS communication
    rclpy.shutdown()


if __name__ == '__main__':
    main()