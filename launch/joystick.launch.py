from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    control_topic = LaunchConfiguration('topic')

    joy_params = os.path.join(get_package_share_directory('robot_teleop'),'config','joystick.yaml')

    control_topic_arg  = DeclareLaunchArgument(
        name='topic',
        description='topic of the robot controller'
    )

    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use sim time if true'
    )

    joy_node = Node(
            package='joy',
            executable='joy_node',
            parameters=[joy_params, {'use_sim_time': use_sim_time}],
         )

    teleop_node = Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_node',
            parameters=[joy_params, {'use_sim_time': use_sim_time}],
            remappings=[('/cmd_vel','/diff_cont/cmd_vel_unstamped')]
         )

    twist_stamper = Node(
            package='robot_teleop',
            executable='twist_stamper',
            parameters=[{'use_sim_time': use_sim_time}],
            remappings=[('/cmd_vel_in','/diff_cont/cmd_vel_unstamped'),
                        ('/cmd_vel_out', control_topic)]
         )


    return LaunchDescription([
        control_topic_arg,
        use_sim_time_arg,
        joy_node,
        teleop_node,
        twist_stamper,
    ])
