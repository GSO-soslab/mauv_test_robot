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
    )  

    # =================================================== #
    # bringup everything related to ros setup for mavu 1
    # =================================================== #
    mauv_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch','include','bringup_mauv_1.launch.py')]),
    )   

    # =================================================== #
    # bringup everything related to ros setup for mauv 2
    # =================================================== #

    mauv_2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch','include','bringup_mauv_2.launch.py')]),
    )

    # =================================================== #
    # bringup everything related to ros setup for mavu 3
    # =================================================== #
    mauv_3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch','include','bringup_mauv_3.launch.py')]),
    )   

    # =================================================== #
    # bringup everything related to ros setup for mauv 4
    # =================================================== #

    mauv_4 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch','include','bringup_mauv_4.launch.py')]),
    )

    vis = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch','include','bringup_visualization.launch.py')]),
    )    

    return LaunchDescription([
        simulation,
        mauv_1,
        mauv_2,
        mauv_3,
        vis,
    ])  

