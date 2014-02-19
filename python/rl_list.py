import os
import itertools

def run(TOP_DIR):

  # Get the packages and launch file names from launch.config
  launch_conf = TOP_DIR + '/config/launch.config'

  with open(launch_conf, 'r') as f:
    launch_files = [line.rpartition(':')[2].rstrip() for line in f]

  with open(launch_conf, 'r') as f:
    identifiers = [(line.rpartition(':')[0].lstrip()) for line in f]

  max_len = max(len(x.replace('.launch','').strip()) for x in identifiers) + 1
  print '\nKnown launch files:\n'
  known = [(('\t' +  i).replace('.launch', '')).ljust(max_len)\
      + ' --> ' + l\
      for i, l in itertools.izip(identifiers, launch_files)]

  print '\n'.join(known)
  print '\n'

  return
