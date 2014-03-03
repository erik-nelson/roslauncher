import os, subprocess

# ******************************************************************************************************************************** #
def run(TOP_DIR, FILENAME):

  FILENAME.replace('.launch', '')

  # Get preferred editor from config/user.conf file
  with open(TOP_DIR + '/config/user.conf') as f:
    editor_line = [line for line in f if 'editor' in line][0]

  EDITOR = editor_line.replace('editor: ', '').rstrip()

  # Find the file that we would like to edit
  launch_conf = TOP_DIR + '/config/launch.config'
  with open(launch_conf, 'r') as f:
    launch_files = [line.rpartition(':')[2].rstrip() for line in f]

  with open(launch_conf, 'r') as f:
    identifiers = [(line.rpartition(':')[0].lstrip()) for line in f]

  if not any(FILENAME in i for i in identifiers):
    print '\nERROR: \"' + FILENAME + '\" is not a valid launch file.'
    print 'Please a launch file from this list, or add to the list with roslauncher -a LAUNCHFILE'

    # Need to reload the file to grab package names as well for error output
    error_list = [ ('\t' + i).replace('.launch', '') for i in identifiers]
    print '\n'.join(error_list)
    print '\n'

    return

  # Get the path to the launch file
  launch_file_idx = min(idx for idx, string in enumerate(identifiers) if FILENAME in string)
  launch_file = launch_files[launch_file_idx]

  # Open the file with the editor
  call_script = EDITOR + ' ' + launch_file
  subprocess.call(call_script, shell=True)

  return
