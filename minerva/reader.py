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
		tbl = div.find('table', {'class':'dataentrytable', 'width':'100%'})
		
		print  len(tbl.findAll('tr'))
		
		matrix = [col.findAll('td') for col in tbl.findAll('tr')]
		m2 = [[cell.text for cell in col] for col in matrix]
		# m3 = [row.remove('\xa0') for row in m2]
		self.table2py2(m2)
		
		return True

	def table2py2(self, matrix):

		# table = fulltable.find('tr')
		# table2 = table.find('tr')
		for line in matrix:
			print len(line)
			if len(line) == 11:
				print line
		rows = iter(matrix)

		headers = 0#[col.next_sibling for col in rows.next.findAll('td')]
		print headers


	def table2py(self, text):

		table = etree.XML(text)
		#print(etree.tostring(table, pretty_print=True))
		rows = iter(table)
		headers = [col.text for col in next(rows)]
		print headers
		# for row in rows:
		# 	values = [col.text for col in row]
		# 	print values
		# 	#print dict(zip(headers, values))