from setuptools import find_packages, setup

package_name = 'robot_controller_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Solo si quieres usar launch desde aquí también
        #('share/' + package_name + '/launch', ['launch/coppelia_vision_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    include_package_data=True,  # ✅ Para archivos adicionales como launch
    maintainer='alfonso',
    maintainer_email='A00838034@tec.mx',
    description='Nodo controlador que envía comandos de movimiento desde ROS 2 a CoppeliaSim',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_robot_controller = robot_controller_pkg.node_robot_controller:main',
            'circle_controller = robot_controller_pkg.circle_controller:main',
            'node_trajectory_controller = robot_controller_pkg.node_trajectory_controller:main',
            'node_circle_controller = robot_controller_pkg.node_circle_controller:main'
        ],
    },
)
