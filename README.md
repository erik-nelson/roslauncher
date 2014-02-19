# roslauncher:

## A python-based roslaunch utility

## To download:

  cd ~/DOWNLOAD_PATH
  git clone git@nmichael.frc.ri.cmu.edu:enelson/roslauncher.git

## Uses:

Get a list of available flags

      ./roslauncher -h

Scan a ROS/catkin directory and cache launch files beneath it:

      ./roslauncher -s DIRECTORY

Get a list of launch files available for editing and/or launching

      ./roslauncher --list

Launch a launch file known to roslauncher (to see a list of files known to roslauncher, use ./roslauncher --list)

      ./roslauncher -l ROS_PACKAGE/LAUNCH_FILE

For example to launch the test.launch file in the ROS package named example_graph_slam:

      ./roslauncher -l example_graph_slam/test

Edit a launch file in a text editor

      ./roslauncher -e ROS_PACKAGE/LAUNCH_FILE

Add a launch file: NOT CURRENTLY SUPPORTED

      ./roslauncher -a ROS_PACKAGE/LAUNCH_FILE

Rename a launch file: NOT CURRENTLY SUPPORTED

      ./roslauncher -r ROS_PACKAGE/LAUNCH_FILE

Launch roslauncher in terminal menu mode: NOT CURRENTLY SUPPORTED

      ./roslauncher
