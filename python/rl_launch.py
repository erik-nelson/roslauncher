import os, subprocess

# ******************************************************************************************************************************** #
def run(TOP_DIR, FILENAME):

  FILENAME.replace('.launch', '')

  # Get the packages and launch file names from launch.config
  launch_conf = TOP_DIR + '/config/launch.config'

  with open(launch_conf, 'r') as f:
    launch_files = [line.rpartition(':')[2].rstrip() for line in f]

  with open(launch_conf, 'r') as f:
    identifiers = [(line.rpartition(':')[0].lstrip()) for line in f]

  if not any(FILENAME in i for i in identifiers):
    print '\nERROR: \"' + FILENAME + '\" is not a valid launch file.'
    print 'Please select a launch file from this list, or add to the list with roslauncher -a LAUNCHFILE'

    error_list = [ ('\t' + i).replace('.launch', '') for i in identifiers]
    print '\n'.join(error_list)
    print '\n'

    return

  # Get the path to the launch file
  launch_file_idx = min(idx for idx, string in enumerate(identifiers) if FILENAME in string)
  launch_file = launch_files[launch_file_idx]

  # Launch the file with subprocess
  subprocess.call('roslaunch ' + launch_file, shell=True)

  return
