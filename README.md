# Roslauncher:

## A python-based roslaunch utility

## Description:

Roslauncher is a utility designed to simplify the hassle of dealing with editing and launching Robot Operating System (ROS) launch files. It allows a user to scan their catkin directory hierarchy for all files containing ".launch", caches the paths to those files, and then enables launch file editing and launching from anywhere. In addition, rosparam files included in a launch file can be edited by adding the '-p' flag. The root folder of the catkin package can be re-specified at any time with the '-s' flag. See below for additional functionality.

## To download:

      cd ~/DOWNLOAD_PATH
      git clone https://github.com/enelsonCMU/roslauncher.git

To call roslauncher from anywhere, set up an alias in your .bashrc file (remember to change DOWNLOAD_PATH in the command below)

      echo "alias roslauncher='PYTHONPATH=${PYTHONPATH}:~/DOWNLOAD_PATH/python python ~/DOWNLOAD_PATH/roslauncher" >> ~/.bashrc

## Uses:

Get a list of available flags

      ./roslauncher.py -h


Scan a ROS/catkin directory and cache launch files beneath it:

      ./roslauncher.py -s DIRECTORY


Get a list of launch files available for editing and/or launching

      ./roslauncher.py -l


Launch a launch file known to roslauncher (to see a list of files known to roslauncher, use ./roslauncher -l)

      ./roslauncher.py ROS_PACKAGE/LAUNCH_FILE


For example, to launch the test.launch file in the ROS package named example_graph_slam:

      ./roslauncher.py example_graph_slam/test


Edit a launch file in a text editor

      ./roslauncher.py -e ROS_PACKAGE/LAUNCH_FILE


Add a launch file without needing to re-scan the catkin workspace: NOT CURRENTLY SUPPORTED

      ./roslauncher.py -a ROS_PACKAGE/LAUNCH_FILE


Rename a launch file: NOT CURRENTLY SUPPORTED

      ./roslauncher.py -r ROS_PACKAGE/LAUNCH_FILE
