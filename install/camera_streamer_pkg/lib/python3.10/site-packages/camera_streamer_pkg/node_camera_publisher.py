import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')

        self.bridge = CvBridge()
        self.publisher_ = self.create_publisher(Image, 'camera_image', 10)

        # Conexión con CoppeliaSim
        try:
            client = RemoteAPIClient()
            self.sim = client.getObject('sim')
            self.sensor_handle = self.sim.getObject('/visionSensor')
            self.get_logger().info('✅ Conectado con CoppeliaSim y sensor obtenido')
        except Exception as e:
            self.get_logger().error(f'❌ Error al conectar con CoppeliaSim: {e}')
            return

        # Timer de publicación
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('📷 Nodo de cámara iniciado y publicando...')

    def timer_callback(self):
        try:
            # Obtener imagen cruda
            img, resX, resY = self.sim.getVisionSensorCharImage(self.sensor_handle)
            img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            img = cv2.flip(img, 0)  # Ajuste de orientación

            # Redimensionar imagen para mejor visualización
            img_big = cv2.resize(img, (resX * 2, resY * 2), interpolation=cv2.INTER_LINEAR)

            # Publicar mensaje de imagen
            msg = self.bridge.cv2_to_imgmsg(img_big, encoding='bgr8')
            self.publisher_.publish(msg)

        except Exception as e:
            self.get_logger().warn(f'⚠️ Error en la lectura o publicación de imagen: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = CameraPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
