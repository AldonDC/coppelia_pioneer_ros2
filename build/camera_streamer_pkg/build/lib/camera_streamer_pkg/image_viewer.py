import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageViewer(Node):
    def __init__(self):
        super().__init__('image_viewer')
        self.bridge = CvBridge()
        self.image_received = False
        self.cv_image = None

        self.subscription = self.create_subscription(
            Image,
            'camera_image',
            self.listener_callback,
            10)
        
        self.timer = self.create_timer(0.1, self.update_window)
        self.get_logger().info('🖼️ Nodo de visualización de imagen iniciado')

    def listener_callback(self, msg):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            self.image_received = True
        except Exception as e:
            self.get_logger().error(f"Error al convertir imagen: {e}")

    def update_window(self):
        if self.image_received:
            cv2.imshow("📷 Cámara desde CoppeliaSim", self.cv_image)
            key = cv2.waitKey(1)
            if key == 27:  # Tecla ESC para cerrar
                rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    viewer = ImageViewer()
    try:
        rclpy.spin(viewer)
    except KeyboardInterrupt:
        pass
    finally:
        viewer.destroy_node()
        cv2.destroyAllWindows()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
