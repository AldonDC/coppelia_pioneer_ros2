import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageViewer(Node):
    def __init__(self):
        super().__init__('image_viewer')
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            'camera_image',
            self.listener_callback,
            10)
        self.get_logger().info('🖼️ Nodo de visualización de imagen iniciado')

    def listener_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            cv2.imshow("Cámara desde CoppeliaSim", cv_image)
            cv2.waitKey(1)
        except Exception as e:
            self.get_logger().error(f"Error al convertir imagen: {e}")

def main(args=None):
    rclpy.init(args=args)
    viewer = ImageViewer()
    try:
        rclpy.spin(viewer)
    except KeyboardInterrupt:
        pass
    viewer.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
