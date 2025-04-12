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
│   ├── node_circle_controller.py   # Genera trayectorias (círculo, zigzag, cuadrado)
│   └── robot_controller.py             # Control manual puro por ZMQ (modo test)
├── launch/
│   └── coppelia_vision_launch.py       # Lanza todos los nodos ROS 2 necesarios
```

---

## 🎯 Objetivos del proyecto

- ✅ Controlar un robot Pioneer P3DX en simulación 3D.
- ✅ Ejecutar trayectorias predefinidas: círculo, zigzag, cuadrado.
- ✅ Visualizar el entorno mediante un sensor de cámara virtual.
- ✅ Validar cálculos de cinemática inversa diferencial.
- ✅ Simular comunicación realista entre ROS 2 y CoppeliaSim con ZMQ.

---

## 🧪 Simulación realizada

- **Robot simulado:** Pioneer P3DX
- **Sensado visual:** Sensor de visión vinculado a un nodo ROS 2
- **Trayectorias implementadas:**
  - `circle`: Gira en una trayectoria circular.

---

## 🚀 Instrucciones de uso

### 1. Lanzar CoppeliaSim

- Abre `PRUEBA1.ttt` en CoppeliaSim
- Presiona el botón ▶️ para iniciar la simulación

### 2. Construir el workspace

```bash
cd ~/coppelia_vision_control_ws
colcon build
source install/setup.bash
```

### 3. Ejecutar la simulación

```bash
ros2 launch camera_streamer_pkg coppelia_vision_launch.py
```

---

## 🖼 Visualización de la cámara

Para ver la imagen publicada por el sensor de visión:

```bash
ros2 run rqt_image_view rqt_image_view
```

Selecciona el topic `/camera_image` en el menú desplegable de la interfaz.

---

## 🎥 Video demostrativo

> 💡 A continuación se muestra una breve demostración del robot en movimiento siguiendo una trayectoria circular en CoppeliaSim:

🔽 Puedes reproducir el video directamente aquí (si tu visor lo permite):

<video controls width="100%">
  <source src="media/SIMULACION_CERON1.mp4" type="video/mp4">
  Tu navegador no soporta la visualización de video embebido.
</video>



---

## 📸 Captura de la cámara simulada

<div align="center">
  <img src="https://github.com/user-attachments/assets/a5ef6ca4-9dbe-425e-9a94-2864dcdc5bb8" alt="Vista desde cámara del Pioneer P3DX" width="800"/>
  <p><i>Vista en tiempo real desde el sensor de visión en CoppeliaSim 🎥🤖</i></p>
</div>



---

## 👨‍💻 Autor

**Alfonso Solís Díaz**  
Estudiante de Ingeniería en Robótica y Sistemas Digitales  
Tecnológico de Monterrey

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia [MIT](https://opensource.org/licenses/MIT).
