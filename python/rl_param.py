import os, subprocess

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
    print 'Please a launch file from this list, or add to the list with roslauncher -a LAUNCHFILE'

    error_list = [ ('\t' + i).replace('.launch', '') for i in identifiers]
    print '\n'.join(error_list)
    print '\n'

    return

  # Get the path to the launch file
  launch_file_idx = min(idx for idx, string in enumerate(identifiers) if FILENAME in string)
  launch_file = launch_files[launch_file_idx].lstrip()

  # Search the launch file for lines with "rosparam file"
  with open(launch_file, 'r') as f:
    rosparam_files = [l for l in f if 'rosparam file' in l];

  # If there are no rosparam files in the launch file, exit
  if (len(rosparam_files) is 0):
    print '\tLaunch file \"' + FILENAME + '\" contains no rosparam files'
    return

  # Remove formatting and mold into a readable string with package/filename
  rosparam_files = [l.strip().rpartition('$')[2] for l in rosparam_files]
  rosparam_files = [l.replace('(find ', '') for l in rosparam_files]
  rosparam_files = [l.replace(')', '') for l in rosparam_files]
  rosparam_files = [l.replace('"/>', '') for l in rosparam_files]

  # Remove duplicates
  rosparam_files = list(set(rosparam_files))

  # Present the parameter files to the user in a list
  print '\n\tSelect a parameter file to edit\n'
  print '\t(0) EXIT'
  for num, pfile in enumerate(rosparam_files):
    print '\t(' + str(num+1) + ') ' +  pfile

  # Get the file to edit from the user
  sel = int(raw_input('\t>> '))
  if (sel is 0):
    print '\n\tExiting.\n'
    return
  else:
    param_file = rosparam_files[sel-1]
    print '\n\tEditing file \"' + param_file + '\"'

    # We are going to edit the file. Get the preferred editor of the user
    with open(TOP_DIR + '/config/user.config') as f:
      editor_line = [line for line in f if 'editor' in line][0]
    with open(TOP_DIR + '/config/user.config') as f:
      ros_dir = [line for line in f if 'ros_dir' in line][0]

    EDITOR = editor_line.replace('editor: ', '').rstrip()
    LAUNCH_DIR = ros_dir.replace('ros_dir: ', '').rstrip()

    package = param_file.partition('/')[0]
    param = param_file.rpartition('/')[2]

    # Make a shell command to edit the specified file
    call_script = EDITOR
    call_script += ' $(find '
    call_script += LAUNCH_DIR
    call_script += ' -name \"'
    call_script += param
    call_script += '\" | grep \"'
    call_script += package
    call_script += '\")'

    # Edit the file with the user's preferred text editor
    subprocess.call(call_script, shell=True)

  print '\n'

  return
