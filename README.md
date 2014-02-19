# roslauncher:

A python-based roslaunch utility

To download:

'''sh
cd ~/DOWNLOAD_PATH
git clone git@nmichael.frc.ri.cmu.edu:enelson/roslauncher.git
'''

Uses:

* Get a list of available flags
'''sh
./roslauncher -h
'''

* Scan a ROS/catkin directory and cache launch files beneath it:
'''sh
./roslauncher -s DIRECTORY
'''

* Get a list of launch files available for editing and/or launching
'''sh
./roslauncher --list
'''

* Launch a launch file known to roslauncher (to see a list of files known to roslauncher, use ./roslauncher --list)
'''sh
./roslauncher -l ROS_PACKAGE/LAUNCH_FILE
'''

For example to launch the test.launch file in the ROS package named example_graph_slam:
'''sh
./roslauncher -l example_graph_slam/test
'''

* Edit a launch file in a text editor
'''sh
./roslauncher -e ROS_PACKAGE/LAUNCH_FILE
'''

* Add a launch file: NOT CURRENTLY SUPPORTED
'''sh
./roslauncher -a ROS_PACKAGE/LAUNCH_FILE
'''

* Rename a launch file: NOT CURRENTLY SUPPORTED
'''sh
./roslauncher -r ROS_PACKAGE/LAUNCH_FILE
'''

* Launch roslauncher in terminal menu mode: NOT CURRENTLY SUPPORTED
'''sh
./roslauncher
'''
