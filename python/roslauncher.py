#!/usr/bin/env python

# ******************************************************************************************************************************** #
def respawn() :
  python = sys.executable
  os.execl(python, python, * sys.argv)

# ******************************************************************************************************************************** #
def first_run(TOP_DIR) :

  # Check if this is the user's first time. If so, do some configuration
  CONF_DIR = TOP_DIR + '/config'
  if (not os.path.exists(CONF_DIR)):

    # Prompt for ROS stack directory
    print '\nWelcome to roslauncher! Please take a moment to configure some settings.'
    print '\n\tWhat is the absolute path to the top-level of the ROS package stack containing your launch files?'
    print '\t(Example: ~/Git/ros/catkin_ws)'
    ROS_DIR = raw_input('\t>> ')

    # Make sure we have a consistent format
    ROS_DIR = ROS_DIR.replace("~", os.path.expanduser("~"))
    if (ROS_DIR[-1] == '/'):
      ROS_DIR = ROS_DIR.rpartition('/')[0]

    # Scan the directory for all launch files contained within
    if (not rl_scan.run(TOP_DIR, ROS_DIR)):
      print '\tRelaunching startup script. Better luck next time.'
      return True

    # Prompt for default text editor
    print '\n\tWhich text editor would you like to use for editing ROS launch files?'
    print '\t{vim, nano, emacs, gedit, leafpad, notepad++, etc.}'
    EDITOR = raw_input('\t>> ')

    # Write the user-specified configurations to configuration file
    # NOTE: The config folder now exists, since rl_scan created it
    with open(CONF_DIR + '/user.conf', 'w+') as f:
      f.writelines('\n'.join( ['ros_dir: ' + ROS_DIR, 'editor: ' + EDITOR] ) )

    print '\n\n\tThank you. Launching menu.\n\n'

    # It is the user's first time using this program
    return True

  # It is __not__ the user's first time using this program
  return False


# ******************************************************************************************************************************** #
def parse_arguments(TOP_DIR) :

  # Set up flag formatting
  parser = argparse.ArgumentParser()
  parser.add_argument('--list', action='store_true',     help='list all roslaunch known files',                    required=False, dest='list')
  parser.add_argument('-l', '--LAUNCHFILE',          help='launch a roslaunch file',                           required=False, dest='launch')
  parser.add_argument('-e', '--EDITFILE',            help='edit a roslaunch file',                             required=False, dest='edit')
  parser.add_argument('-r', '--RENAMEFILE',          help='rename a roslaunch file',                           required=False, dest='rename')
  parser.add_argument('-s', '--SCANDIR',             help='scan a root directory for launch files beneath it', required=False, dest='scan')
  parser.add_argument('-a', '--ADDFILE',             help='add a roslaunch file',                              required=False, dest='add')

  # Get the user's flags
  args = vars(parser.parse_args())

  # Reroute flags
  try:
    if (args['list']):
      rl_list.run(TOP_DIR)

    elif (args['launch']):
      FILENAME = args['launch']
      rl_launch.run(TOP_DIR, FILENAME)

    elif (args['edit']):
      FILENAME = args['edit']
      rl_edit.run(TOP_DIR, FILENAME)

    elif (args['rename']):
      FILENAME = args['rename']
      rl_rename.run(TOP_DIR, FILENAME)

    elif (args['add']):
      FILENAME = args['add']
      rl_add.run(TOP_DIR, FILENAME)

    elif (args['scan']):
      SCAN_DIR = args['scan']
      rl_scan.run(TOP_DIR, SCAN_DIR)

    else:
      rl_menu.run(TOP_DIR, args)

  except IOError, msg:
    parser.error(str(msg))


# ******************************************************************************************************************************** #
if __name__=='__main__':

  import sys, argparse, os
  sys.dont_write_bytecode = True

  # Import after to prevent .pyc files
  import rl_list,\
         rl_launch,\
         rl_edit,\
         rl_rename,\
         rl_add,\
         rl_menu,\
         rl_scan\

  # Get filepath of root directory
  TOP_DIR = sys.path[0].rpartition('/')[0]

  if ( not first_run(TOP_DIR) ):
    parse_arguments(TOP_DIR)

  else:
    # Restart the program
    respawn()
