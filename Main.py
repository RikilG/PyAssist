# from multiprocessing import Process
from sys import exit as exitPyassist
from sys import platform
import os
import webbrowser

import Help
import Music
import Banner
import Finder
import DailyQuote
import BingWallpaper
import IdleThoughts

plat = None
if platform.startswith('linux'):
	plat = 'linux'
elif platform.startswith('win'):
	plat = 'windows'

print('\n>>>Welcome to PyAssist<<')
if plat == 'linux':
	Banner.showBanner()
print('type "bye" to exit or "help" to print list of commands')
DailyQuote.get_quote()

while(True):
	print('>> How can i help you? : ', end='')

	query = input().lower().split(' ',1)
	if query[0] == 'bye' or query[0] == 'quit' or query[0] == 'exit':
		print('Have a nice Day :)')
		exitPyassist()
		
	#elif query[0] == 'help':
	#	Help.helper(query)

	elif query[0] == 'clear':
		os.system('clear')
	
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
		Finder.find(query[1],plat)
		
	elif 'run' == query[0] or 'start' == query[0]:
		Finder.run(query[1],plat)
	
	elif query[0] == 'open':
		Finder.open(query[1],plat)
		# pass
	
	elif 'music' in query or 'songs' in query or 'song' in query : 
		Music.run_query(query,plat)
	
	# elif 'login' in query:
	#	subprocess.call("%USERPROFILE%\Documents\MyCyberoam.py",shell=True)

	elif 'change'==query[0] and 'wallpaper' in query[1].lower():
		BingWallpaper.get_Wallpaper(plat)
	
	elif ('what'in query and 'do' in query) or 'ideas' in query or 'thoughts' in query or 'idea' in query or 'thought' in query:
		IdleThoughts.run_query(query)
	
	else:
		print('Unrecognized command. please consider improving me.')
