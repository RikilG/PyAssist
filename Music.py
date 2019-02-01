import os

def run_query(query, platform):

	if platform == 'windows':
		# requires musicbee
		if 'pause' in query:
			os.system('start musicbee /PlayPause')
		elif 'next' in query:
			os.system('start musicbee /Next')
		elif 'previous' in query or 'prev' in query:
			os.system('start musicbee /Previous')
		elif 'play' in query:
			os.system('start musicbee /PlayResume')
	
	if platform == 'linux':
		# requires cmus and cmus-remote to be installed
		if 'pause' in query:
			os.system('cmus-remote --pause')
		elif 'next' in query:
			os.system('cmus-remote --next')
		elif 'previous' in query or 'prev' in query:
			os.system('cmus-remote --prev')
		elif 'play' in query:
			os.system('cmus-remote --play')
		