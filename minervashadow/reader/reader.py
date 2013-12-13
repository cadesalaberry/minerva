from bs4 import BeautifulSoup
import login
import transcript

class MinervaReader:

	def __init__(self, site):
		self.site = site

	def login(self, html):

		if html.geturl() == self.site.login:
			print login.welcomeerr(html)
		else:
			print login.welcomemsg(html)

	def transcript(self, html, semester='all'):
		
		soup = BeautifulSoup(html)

		# Gets the div containing the table
		div = soup.body.find('div', {'class':'pagebodydiv'})

		# Gets the table inside that div
		tbl = div.find('table', {'class':'dataentrytable', 'width':'100%'})

		# Turns the html table into a list of lists (2D list)
		table = [col.findAll('td') for col in tbl.findAll('tr')]

		curriculum = transcript.get_curriculum(table)
	
		print curriculum
		
		return True

					
