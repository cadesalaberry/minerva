from HTMLParser import HTMLParser
from urlparse import urlparse
from urlparse import parse_qs
from bs4 import BeautifulSoup
from lxml import etree

class MinervaReader:

	def __init__(self, site):
		self.s = site

	def welcomemsg(self, html):
		query = parse_qs(html.geturl())
		messg = HTMLParser().unescape(query['msg'][0])
		messg = messg.replace('<b>', '\n').replace('</b>', '\n')
		return messg

	def welcomeerr(self, html):
		# Instead we should try reading the error message displayed on the html
		return 'Authorization Failure - you have entered an invalid McGill Username / Password.'

	def transcript(self, html, semester='all'):
		soup = BeautifulSoup(html)

		# div[4] : class="plaintable"		-> title + static header
		# div[5] : class="staticheaders"	-> empty
		# div[7] : class="infotextdiv"		-> Contains error message ?
		# div[8] : class="pagefooterdiv"	-> Form Name: SWFTRAN
		# div[9] : class="poweredbydiv"
		# div[10]: class="div1"				-> empty
		# div[11]: class="div2"				-> empty
		# div[12]: class="div3"				-> empty
		# div[13]: class="div4"				-> empty
		# div[14]: class="div5"				-> empty
		# div[15]: class="div6"				-> empty
		div = soup.body.find('div', {'class':'pagebodydiv'})
		tbl = div.find_all('table', {'class':'dataentrytable'})[-1]
		print tbl.find_all(True)[0]

		# print str(tbl.find('tr')), '<'
		self.table2py2(tbl)
		# soup.body.find_all('div')[-10]
		# tables = div.find_all('table')[-3]
		return True

	def table2py2(self, fulltable):

		table = fulltable.findAll('tr')
		print table[0].text
		rows = iter(table)
		# headers = [col.text
		for i, col in next(rows):print i, col.text
		# ]

		for row in rows:
			cells = row.findAll('td')
			values = [cell.text for cell in cells]
			print values
			#print dict(zip(headers, values))

	def table2py(self, text):

		table = etree.XML(text)
		rows = iter(table)
		headers = [col.text for col in next(rows)]
		print headers
		for row in rows:
			values = [col.text for col in row]
			print values
			#print dict(zip(headers, values))