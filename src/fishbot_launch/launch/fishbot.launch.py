from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='micro_ros_agent',
            executable='micro_ros_agent',
            name='fishbot_agent',
            output='screen',
            emulate_tty=True,
            arguments=["serial","-b", "921600", "--dev", "/dev/ttyUSB1", "-v"]
        )
    ])
