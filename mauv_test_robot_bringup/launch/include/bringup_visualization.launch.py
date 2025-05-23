
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os

def generate_launch_description(): 

    rviz_config_dir = os.path.join( 
        get_package_share_directory('mauv_test_robot_description'), 'config', 'config.rviz' )
    # rqt_config_dir = os.path.join( 
    #     get_package_share_directory('mauv_test_robot_description'), 'config', 'rqt.perspective' )

    return LaunchDescription([

        # connect the mauv_1 and mauv_2
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='mauv_1_mauv_2',
            arguments = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", 'mauv_1/world', 'mauv_2/world'] 
            # arguments = ["30.0", "-30.0", "0.0", "0.0", "0.0", "0.0", 'mauv_1/world', 'mauv_2/world']

   
        ),

        # connect world and world_ned for mauv1
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='mauv_1_world_ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", 'mauv_1/world', 'mauv_1/world_ned']    
        ),

        # connect world and world_ned for mauv2
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='mauv_2_world_ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", 'mauv_2/world', 'mauv_2/world_ned']    
        ),        

        # connect odom to world for mauv_1 to support RViz fixed frame
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='mauv1_odom_to_world',
        #     arguments=["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", 'mauv_1/odom', 'mauv_1/world']
        # ),

        # rviz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2', 
            arguments=['-d', [rviz_config_dir]],
        ),

        # # rqt
        # Node(package="rqt_gui", 
        #      executable="rqt_gui", 
        #      name="rqt", 
        #      arguments=["--perspective-file", rqt_config_dir],
        # ),
])
