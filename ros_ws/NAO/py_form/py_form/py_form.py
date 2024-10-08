# import all needed Librarys
import rclpy

# handles creation of nodes
from rclpy.node import Node

# enables all needed data types
from std_msgs.msg import String    # std_msgs equals standard messages

# create main class
class Form(Node):
    # create a class as a subclass of the class constructor to setup the node
    def __init__(self):
        # initiate the Node class's constructor and name it
        super().__init__('form')

        # create the publisher | this will publish a String to the addison topic
        self.publisher_ = self.create_publisher(String, 'addison', 10)  # (msg.type, topic, queue size as integer)

        # it will be published a message every 0.5 seconds
        timer_period = 0.5 

        # create a timer
        self.timer = self.create_timer(timer_period, self.timer_callback)  # (timer_period, callback)

        # initiate a counter variable
        self.i = 0

    def timer_callback(self):
        # callback function | this function gets called every 0.5 seconds

        # create a string message
        msg = String()

        # set the string message's data
        msg.data = "Hi ich bin Jannis und das zum %d" % self.i

        # publish the message to the topic
        self.publisher_.publish(msg)

        # display the message as an output
        self.get_logger().info(f"Hey ich hab folgendes gepublisht: {msg.data}")

        # count the repetition
        self.i += 1

    def main(args=None):

        # initiate rclpy library
        rclpy.init(args=args)

        # initiate Node
        py_form = Form()

        # running node
        rclpy.spin(form)
        
        # stops node
        form.destroy_node()

        # clears memory
        rclpy.shutdown()

# if name of the pkg equals name of the main class
if __name__ == "__main__":
    main()