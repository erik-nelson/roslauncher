import os, fileinput

# ******************************************************************************************************************************** #
def scan(SCAN_DIR):

  # Walk through the file hierarchy and return all filenames
  for path, dirs, files in os.walk(SCAN_DIR):
    for f in files:
      yield os.path.join(path, f)

# ******************************************************************************************************************************** #
def store(TOP_DIR, SCAN_DIR, launch_files):

  # Open up the config file and update
  print '\tUpdating launch.config'

  # Make a config folder if it does not exist yet
  if (not os.path.exists(TOP_DIR + '/config')):
      os.makedirs(TOP_DIR + '/config')

  # Remove the old config file
  CONFIG_FILE = TOP_DIR + '/config/launch.config'
  if (os.path.exists(CONFIG_FILE)):
    os.remove(CONFIG_FILE)

  # Write out the new config file
  with open(CONFIG_FILE, 'w+') as f:
    for launch in launch_files:
      package, filename = launch.split('/')[-3], (launch.split('/')[-1]).rstrip()
      line = package + '/' + filename + ': ' + launch + '\n'
      f.write(line)

  # Replace the old launch file top directory from user.config
  USER_FILE = TOP_DIR + '/config/user.config'
  if (os.path.exists(USER_FILE)):
    for line in fileinput.input(USER_FILE, inplace=1):
      if 'ros_dir' in line:
        print 'ros_dir: ' + SCAN_DIR
      else:
        print line

  # Print some user output saying which files we found
  print '\n\tFound the following launch files:'
  found = [('\t' + launch) for launch in launch_files]
  print '\n'.join(found)
  print '\n'

# ******************************************************************************************************************************** #
def run(TOP_DIR, SCAN_DIR):

  if (not os.path.exists(SCAN_DIR)):
      print '\nERROR: directory \"' + SCAN_DIR + '\" does not exist'
      return False

  print '\n\tOne moment, scanning path \"' + SCAN_DIR + '\" for launch files'

  launch_files = [f for f in scan(SCAN_DIR) if f.endswith('.launch')]
  store(TOP_DIR, SCAN_DIR, launch_files)

  print '\tScan complete!'

  return True
