import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
import time


def generate_launch_description():

    arg_robot_name = 'mauv_test_robot'
    robot_bringup = arg_robot_name + '_bringup'

    # =================================================== #
    # bringup everything related to stonefish simulator
    # =================================================== #

    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch','include','bringup_stonefish.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )  

    # =================================================== #
    # bringup everything related to ros setup for mavu 1
    # =================================================== #
    mauv_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch','include','bringup_mauv_1.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )   

    # =================================================== #
    # bringup everything related to ros setup for mauv 2
    # =================================================== #

    mauv_2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch','include','bringup_mauv_2.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )

    # =================================================== #
    # bringup everything related to ros setup for mavu 3
    # =================================================== #
    mauv_3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch','include','bringup_mauv_3.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )   

    # =================================================== #
    # bringup everything related to ros setup for mauv 4
    # =================================================== #

    mauv_4 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch','include','bringup_mauv_4.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )

    vis = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch','include','bringup_visualization.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )    

    return LaunchDescription([
        simulation,
        mauv_1,
        mauv_2,
        mauv_3,
        mauv_4,
        vis,
    ])  


    # =================================================== #
    # old version one mauv
    # =================================================== #

    # # simulation
    # simulation = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','simulation.launch.py')]),
    #     launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    # )

    # # robot localization
    # localization = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','localization.launch.py')]),
    #     launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    # )
        
    # #description URDF
    # description = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','description.launch.py')]),
    #     launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    # )


    # #mvp_control
    # mvp_control = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','mvp_control.launch.py')]),
    #     launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    # )

    # #mvp_mission
    # mvp_mission = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','mvp_mission.launch.py')]),
    #     launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    # )

    # #joy
    # joy = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','joy.launch.py')]),
    #     launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    # )

    # usbl_test = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','usbl.launch.py')]),
    #     launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    # )

    #     # ld.extend([
    #     #     simulation,
    #     #     localization,
    #     #     description,
    #     #     mvp_control,
    #     #     mvp_mission,
    #     #     joy,
    #     #     # usbl_test  # Uncomment if needed
    #     # ])

    # # return LaunchDescription(ld)

    # return LaunchDescription([
    #     simulation,
    #     localization,
    #     description,
    #     mvp_control,
    #     mvp_mission,
    #     # usbl_test
    #     joy
    # ])




