# launch/coppelia_vision_launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='camera_streamer_pkg',
            executable='node_camera_publisher',
            name='camera_node',
            output='screen'
        ),
        Node(
            package='coppelia_bridge_pkg',
            executable='image_streamer',
            name='image_streamer_node',
            output='screen'
        ),
        Node(
            package='robot_controller_pkg',
            executable='node_robot_controller',
            name='robot_controller_node',
            output='screen'
        ),
        Node(
            package='robot_controller_pkg',
            executable='node_circle_controller',
            name='circle_controller_node',
            output='screen'
        )
    ])
