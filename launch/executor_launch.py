from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='MultiThreadedExecutor',
            executable='executor_node',
            name='parallel_node',
            output='screen'
        )
    ])
