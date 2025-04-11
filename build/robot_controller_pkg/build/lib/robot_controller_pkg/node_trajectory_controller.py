import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TrajectoryController(Node):
    def __init__(self):
        super().__init__('trajectory_controller')

        # Solo trayectoria circular
        self.trajectory_type = 'circle'
        self.get_logger().info(f'🚗 Trayectoria seleccionada: {self.trajectory_type}')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Hz
        self.time_counter = 0.0

    def timer_callback(self):
        msg = Twist()
        self.time_counter += 0.1

        # Movimiento circular simple (usando ruedas)
        msg.linear.x = 0.1
        msg.angular.z = 0.8

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()