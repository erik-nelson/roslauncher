# Roslauncher:

## A python-based roslaunch utility

## To download:

      cd ~/DOWNLOAD_PATH
      git clone git@nmichael.frc.ri.cmu.edu:enelson/roslauncher.git

## Uses:

Get a list of available flags

      ./roslauncher.py -h



Scan a ROS/catkin directory and cache launch files beneath it:

      ./roslauncher.py -s DIRECTORY



Get a list of launch files available for editing and/or launching

      ./roslauncher.py -l



Launch a launch file known to roslauncher (to see a list of files known to roslauncher, use ./roslauncher --list)

      ./roslauncher.py ROS_PACKAGE/LAUNCH_FILE



For example to launch the test.launch file in the ROS package named example_graph_slam:

      ./roslauncher.py example_graph_slam/test



Edit a launch file in a text editor

      ./roslauncher.py -e ROS_PACKAGE/LAUNCH_FILE



Add a launch file: NOT CURRENTLY SUPPORTED

      ./roslauncher.py -a ROS_PACKAGE/LAUNCH_FILE



Rename a launch file: NOT CURRENTLY SUPPORTED

      ./roslauncher.py -r ROS_PACKAGE/LAUNCH_FILE


To call roslauncher from anywhere, set up an alias in your .bashrc file

      echo "alias roslauncher='PYTHONPATH=${PYTHONPATH}:~/PATH_TO_ROSLAUNCHER/python python ~/PATH_TO_ROSLAUNCHER/roslauncher" >> ~/.bashrc
