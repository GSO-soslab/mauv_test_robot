import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource



def generate_launch_description():
    # robot_name = 'mauv_test_robot'
    # robot_bringup = robot_name + '_bringup'
    
    sim_world = 'mauv_world.scn'

    world_of_stonefish_dir = get_package_share_directory('world_of_stonefish')

    simulation_data = os.path.join(world_of_stonefish_dir, 'data/')
    scenario_desc = os.path.join(world_of_stonefish_dir, 'world', sim_world)
    simulation_rate = "100"
    window_res_x = "1200"
    window_res_y = "800"
    rendering_quality ="low"

    # ======================================================================= #
    # simulation node
    # ======================================================================= #
    stonefish = Node(
        package="stonefish_ros2",
        executable="stonefish_simulator",
        name="stonefish_simulator",
        # output="screen",
        arguments=[
            simulation_data, scenario_desc, simulation_rate, 
            window_res_x, window_res_y, rendering_quality]
    )

    # ======================================================================= #
    # bringup simulated vehicles
    # ======================================================================= #
    robot_bringup = 'mauv_test_robot_bringup'

    # bringup the first mauv 
    sim_mauv_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup),
            'launch', 'include', 'mauv_1', 'mauv_1.launch.py')]),
        launch_arguments = {
            'arg_vehicle_name': 'mauv_1',
            'arg_world_frame': 'mauv_1/world',
            'arg_imu_frame': 'mauv_1/imu_sf'
            
        }.items()    
    )   

    # bringup the second mauv
    sim_mauv_2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup),
            'launch', 'include', 'mauv_2', 'mauv_2.launch.py')]),
        launch_arguments = {
            'arg_vehicle_name': 'mauv_2',
            'arg_world_frame': 'mauv_2/world',
            'arg_imu_frame': 'mauv_2/imu_sf'
        }.items()    
    )  

    # bringup the third mauv 
    sim_mauv_3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup),
            'launch', 'include', 'mauv_3', 'mauv_3.launch.py')]),
        launch_arguments = {
            'arg_vehicle_name': 'mauv_3',
            'arg_world_frame': 'mauv_3/world',
            'arg_imu_frame': 'mauv_3/imu_sf'
            
        }.items()    
    )   

    # bringup the fourth mauv
    sim_mauv_4 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup),
            'launch', 'include', 'mauv_4', 'mauv_4.launch.py')]),
        launch_arguments = {
            'arg_vehicle_name': 'mauv_4',
            'arg_world_frame': 'mauv_4/world',
            'arg_imu_frame': 'mauv_4/imu_sf'
        }.items()    
    )  

    # ======================================================================= #
    # all the nodes
    # ======================================================================= #
    return LaunchDescription([
        stonefish,
        sim_mauv_1,
        sim_mauv_2,
        sim_mauv_3,
        sim_mauv_4,
    ])







    # robot_param_path = os.path.join(
    #     get_package_share_directory(robot_bringup),
    #     'config'
    #     )

    # stonefish_driver_param_file = os.path.join(robot_param_path, 'sim_params.yaml') 





    # return LaunchDescription([
    #     # simulation node
    #     Node(
    #         package="stonefish_ros2",
    #         executable="stonefish_simulator",
    #         name="stonefish_simulator",
    #         # output="screen",
    #         arguments=[simulation_data, scenario_desc, simulation_rate, window_res_x, window_res_y, rendering_quality]
    #     ),

    #     Node(
    #         package="world_of_stonefish",
    #         executable="imu_driver_node",
    #         namespace=robot_name,
    #         name="imu_driver_node",
    #         remappings=[
    #                 ('imu_in/data', 'imu/stonefish/data'),
    #                 ('imu_out/data', 'imu/data'),
    #             ],
    #         parameters=[
    #             {'frame_id': robot_name + '/imu_sf'},
    #             stonefish_driver_param_file
    #             ]
    #     ),

    #     Node(
    #         package="world_of_stonefish",
    #         executable="thruster_driver_node",
    #         namespace=robot_name,
    #         name="thruster_driver_node",
    #         # prefix=['stdbuf -o L'],
    #         # output="screen",
    #         parameters=[stonefish_driver_param_file]
    #     ),

    #     Node(
    #         package="world_of_stonefish",
    #         executable="dvl_driver_node",
    #         namespace=robot_name,
    #         name="dvl_driver_node",
    #         parameters=[stonefish_driver_param_file]
    #     ),

    #     Node(
    #         package="world_of_stonefish",
    #         executable="pressure_sensor_node",
    #         namespace=robot_name,
    #         name="pressure_sensor_node",
    #         parameters=[
    #             {'frame_id': robot_name + '/world'}]
    #     ),

    #     Node(
    #         package="world_of_stonefish",
    #         executable="usbl_driver_node",
    #         namespace=robot_name,
    #         name="usbl_driver_node",
    #         # parameters=[
    #             # {'frame_id': robot_name + '/world'}
    #             # ]
    #     )

    # ])