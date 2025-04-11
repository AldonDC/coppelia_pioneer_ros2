import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleController(Node):
    def __init__(self):
        super().__init__('circle_controller')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        # Publicar cada 0.1 segundos
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.move_in_circle)
        self.get_logger().info('🌀 Iniciando movimiento circular...')

    def move_in_circle(self):
        msg = Twist()
        msg.linear.x = 0.1  # velocidad lineal
        msg.angular.z = 0.2  # velocidad angular (dirección horaria o antihoraria)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CircleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
