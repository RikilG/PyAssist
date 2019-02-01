import csv

# help commands stored in help_commands.json file
# this is incomplete
def helper(query) :
	try : 
		tmp = query[1].split()
		if(tmp[0]!='add') :
			help_command(tmp)
		else :
			if(tmp[1]!=None and tmp[2]!=None) :
				add_help_command(tmp[1],tmp[2])
	except : 
		print_commands()

def print_commands() :
	print()
	with open("help_commands.csv", newline='') as csvFile :
		commands = csv.reader(csvFile, dialect='excel')
		for command in commands :
			print('\t' + '\t-\t'.join(command))
	print()

def help_command(cmd) :
	print()
	with open("help_commands.csv", newline='') as csvFile :
		commands = csv.reader(csvFile)
	for command in commands :
		str1 = '\t-\t'.join(command)
		if cmd in str1 :
			print('\t' + str1)
	print()

def add_help_command(key,value) :
	with open("help_commands.csv", 'a', newline='') as csvFile :
		spamwriter = csv.writer(csvFile, dialect='excel', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([key] + [value])
	print('successfully added to help menu')