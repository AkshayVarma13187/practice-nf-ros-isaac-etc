import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MathProcessorNode(Node):
    def __init__(self):
        super().__init__('math_processor_node')
        self.subscription = self.create_subscription(Int32, 'input_number', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Int32, 'output_squared', 10)
        self.get_logger().info('Math Processor Node has started. Awaiting Numbers...')

    def listener_callback(self, msg):
        input_val = msg.data
        squared_val = input_val ** 2
        self.get_logger().info(f'Received: {input_val} -> Squaring it to: {squared_val}')

        reply_msg = Int32()
        reply_msg.data = squared_val
        self.publisher_.publish(reply_msg)

def main(args=None):
    rclpy.init(args=args)
    node = MathProcessorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
