from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    fishbot_motion_control_microros_node = Node(
            package='micro_ros_agent',
            executable='micro_ros_agent',
            name='fishbot_motion_control_microros_node',
            output='screen',
            emulate_tty=True,
            arguments=["udp4", "-p", "8888", "-v"]
        )
    return LaunchDescription([
        fishbot_motion_control_microros_node,
    ])
