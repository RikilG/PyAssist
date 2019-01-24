import os

def run_query(query):

	if 'pause' in query:
		os.system('start musicbee /PlayPause')
	elif 'next' in query:
		os.system('start musicbee /Next')
	elif 'previous' in query or 'prev' in query:
		os.system('start musicbee /Previous')
	elif 'play' in query:
		os.system('start musicbee /PlayResume')