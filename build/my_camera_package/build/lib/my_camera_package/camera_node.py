import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.publisher_ = self.create_publisher(Image, '/camera/color/image_raw', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Camera Node has been started.')

    def timer_callback(self):
        msg = Image()
        # Here you can add code for handling camera data
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing Camera Data')

def main(args=None):
    rclpy.init(args=args)
    camera_node = CameraNode()

    rclpy.spin(camera_node)

    camera_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()  # Ensure this line is correctly indented with 4 spaces

