# 🧠 coppelia_pioneer_ros2

**Simulación y control del robot Pioneer P3DX en CoppeliaSim utilizando ROS 2 Humble y la API remota ZMQ.**

Este proyecto integra un entorno completo de simulación y control para un robot móvil tipo Pioneer P3DX, permitiendo enviar trayectorias definidas desde ROS 2 a CoppeliaSim para validar su movimiento mediante comandos de velocidad.

---

## 🛠 Tecnologías utilizadas

- 🧪 CoppeliaSim EDU (v4.5 o superior)
- 🤖 ROS 2 Humble
- 🐍 Python 3.10+
- 🔌 ZMQ Remote API
- 📦 geometry_msgs/Twist
- 🧩 Visual Studio Code (extensiones de Python y ROS)

---

## 📦 Estructura del proyecto

```bash
coppelia_vision_control_ws/
├── camera_streamer_pkg/
│   └── node_camera_publisher.py        # Publica imágenes desde el sensor de visión de CoppeliaSim
├── coppelia_bridge_pkg/
│   └── image_streamer.py               # Conecta la visión desde ZMQ a ROS 2
├── robot_controller_pkg/
│   ├── node_robot_controller.py        # Calcula velocidades de ruedas a partir de /cmd_vel
│   ├── node_trajectory_controller.py   # Genera trayectorias (círculo, zigzag, cuadrado)
│   └── robot_controller.py             # Control manual puro por ZMQ (modo test)
├── launch/
│   └── coppelia_vision_launch.py       # Lanza todos los nodos ROS 2 necesarios
