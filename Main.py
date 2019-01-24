# from multiprocessing import Process
from sys import exit as exitPyassist
import webbrowser

import Help
import Music
import Finder
import download
import DailyQuote
import BingWallpaper

print('\n>>>Welcome to PyAssist<<\n')
print('type "bye" to exit or "help" to print list of commands')
DailyQuote.get_quote()

while(True):
	print('>> How can i help you? : ', end='')

	query = input().lower().split(' ',1)
	if query[0] == 'bye' or query[0] == 'quit' or query[0] == 'exit':
		print('Have a nice Day :)')
		exitPyassist()
		
	elif query[0] == 'help':
		Help.helper(query)
	
	elif query[0] == 'g' or query[0] == 'google':
		if len(query)>1:
			webbrowser.open('http://www.google.com/search?q='+query[1])
		else:
			webbrowser.open('http://www.google.com/search?q=')
	
	elif query[0] == 'ddg' or query[0] == 'duckduckgo':
		if len(query)>1:
			webbrowser.open('http://www.duckduckgo.com/'+query[1])
		else:
			webbrowser.open('http://www.duckduckgo.com/')

	elif query[0] == 'find':
		Finder.find(query[1])
		
	elif 'run' == query[0] or 'start' == query[0]:
		Finder.run(query[1])
	
	elif query[0] == 'open':
		Finder.open(query[1])
		# pass
	
	elif 'music' in query or 'songs' in query or 'song' in query : 
		Music.run_query(query)
	
	elif 'download' == query[0]:
		download.download(query)
	
	# elif 'login' in query:
	#	subprocess.call("%USERPROFILE%\Documents\MyCyberoam.py",shell=True)

	elif 'change'==query[0] and 'wallpaper' in query[1].lower():
		BingWallpaper.get_Wallpaper()
	
	else:
		print('Unrecognized command. please consider improving me.')
