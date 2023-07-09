import os
import time
import pidfile
import constants




def main_loop():
	while True:

		

		complete_files = []
		for root, dir_names, file_names in os.walk(constants.IMAGE_PATH):
			for f in file_names:
      			# This os.path.join() is the most crucial line of all.
				# This line internally implements something DFS style.
				complete_files.append(os.path.join(root, f))
	
		for file in complete_files:
			print(file)
			cmd = "fbi -d /dev/fb0 -T 1 -noverbose -a " + file
			os.system(cmd)
			time.sleep(constants.SECONDS_INTERVAL)

try:
	print(constants.PIDFILE)
	with pidfile.PIDFile(constants.PIDFILE):
		print('Process started')
		main_loop()
except pidfile.AlreadyRunningError:
    print('Already running.')
    sys.exit(0)
