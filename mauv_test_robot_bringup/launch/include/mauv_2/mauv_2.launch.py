import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    robot_name = 'mauv_test_robot'
    robot_bringup = robot_name + '_bringup'

    vehicle_name = LaunchConfiguration('arg_vehicle_name')
    arg_vehicle = DeclareLaunchArgument(
        'arg_vehicle_name',
        default_value='mauv_2'
    )

    world_frame = LaunchConfiguration('arg_world_frame')
    arg_world_frame = DeclareLaunchArgument(
        'arg_world_frame',
        default_value='mauv_2/world'
    )

    imu_frame = LaunchConfiguration('arg_imu_frame')
    arg_sensor_frame = DeclareLaunchArgument(
        'arg_imu_frame',
        default_value='mauv_2/imu_sf' 
    )

    robot_param_path = os.path.join(
        get_package_share_directory(robot_bringup),
        'config'
        )

    # stonefish_driver_param_file = os.path.join(robot_param_path, vehicle_name, 'sim_params.yaml') 
    stonefish_driver_param_file = PathJoinSubstitution([
        get_package_share_directory(robot_bringup),
        'config',
        vehicle_name,
        'sim_params.yaml'
    ])


    # sim_world = 'fls_world.scn'

    # world_of_stonefish_dir = get_package_share_directory('world_of_stonefish')

    # simulation_data = os.path.join(world_of_stonefish_dir, 'data/')
    # scenario_desc = os.path.join(world_of_stonefish_dir, 'world', sim_world)
    # simulation_rate = "100"
    # window_res_x = "1200"
    # window_res_y = "800"
    # rendering_quality ="low"



    return LaunchDescription([
        # # simulation node
        # Node(
        #     package="stonefish_ros2",
        #     executable="stonefish_simulator",
        #     name="stonefish_simulator",
        #     # output="screen",
        #     arguments=[simulation_data, scenario_desc, simulation_rate, window_res_x, window_res_y, rendering_quality]
        # ),

        arg_vehicle,
        arg_world_frame,
        arg_sensor_frame,

        Node(
            package="world_of_stonefish",
            executable="imu_driver_node",
            namespace=vehicle_name,
            name="imu_driver_node",
            remappings=[
                    ('imu_in/data', 'imu/stonefish/data'),
                    ('imu_out/data', 'imu/data'),
                ],
            parameters=[
                {'frame_id': imu_frame},
                stonefish_driver_param_file
                ]
        ),

        Node(
            package="world_of_stonefish",
            executable="thruster_driver_node",
            namespace=vehicle_name,
            name="thruster_driver_node",
            # prefix=['stdbuf -o L'],
            # output="screen",
            parameters=[stonefish_driver_param_file]
        ),

        Node(
            package="world_of_stonefish",
            executable="dvl_driver_node",
            namespace=vehicle_name,
            name="dvl_driver_node",
            parameters=[stonefish_driver_param_file]
        ),

        Node(
            package="world_of_stonefish",
            executable="pressure_sensor_node",
            namespace=vehicle_name,
            name="pressure_sensor_node",
            parameters=[
                {'frame_id': world_frame}]
        ),

        Node(
            package="world_of_stonefish",
            executable="usbl_driver_node",
            namespace=vehicle_name,
            name="usbl_driver_node",
            # parameters=[
                # {'frame_id': robot_name + '/world'}
                # ]
        )

    ])