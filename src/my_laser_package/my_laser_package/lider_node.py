import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LaserNode(Node):
    def __init__(self):
        super().__init__('lider_node')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10
        )
        self.get_logger().info('Laser Node has been started.')

    def listener_callback(self, msg):
        # يمكنك إضافة الكود الخاص بمعالجة بيانات الليزر هنا
        self.get_logger().info('Received Laser Scan Data')

def main(args=None):
    rclpy.init(args=args)
    laser_node = LaserNode()

    rclpy.spin(laser_node)

    laser_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
