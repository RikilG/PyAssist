from datetime import datetime

def get_quote() :
	date = str(datetime.now().date())
	quotes = open("quotes.txt",'r',encoding="ISO-8859-1")
	line = quotes.readline()
	while line is not "":
		if line.split(' ', 1)[0] == date:
			quotation = line.split(' ',1)[1]
			print_quote(quotation)
			quotes.close()
			return None
		line = quotes.readline()
	quotes.close()
	
	print("Getting today's quote. press Ctrl+c to cancel...")
	import requests
	from bs4 import BeautifulSoup
	try:
		page = requests.get("https://theysaidso.com/quote-of-the-day/", timeout=5)
		# page.status_code
		soup = BeautifulSoup(page.content, 'html.parser')
		carousel = soup.find_all(id="myCarousel")
		lead = carousel[0].find_all('div', class_="lead")
		text = lead[0].find('span')
		text = text.get_text()
		author = lead[0].find_all('span')[1]
		author = author.get_text()
		quotation = text+" -"+author
		print_quote(quotation)
		try:
			# write the quote to file.
			with open("quotes.txt",'a') as quotes:
				quotes.write(date + ' ' + text + ' -' + author + "\n")
		except Exception as e:
			print(e)
	except:
		print("Cannot fetch todays quote. Please check your network connection.")

def print_quote(quotation):
	print("\n>>>Todays quote : \n  "+ quotation +"\n")

if __name__ == "__main__":
	get_quote()
