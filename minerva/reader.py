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

		# Gets the div containing the table
		div = soup.body.find('div', {'class':'pagebodydiv'})

		# Gets the table inside that div
		tbl = div.find('table', {'class':'dataentrytable', 'width':'100%'})
	
		self.table2py2(tbl)
		
		return True

	def table2py2(self, tbl):

			
		# Turns the html table into a list of lists (2D)
		html_matrix = [col.findAll('td') for col in tbl.findAll('tr')]

		# Gets rid of the html formatting to get only text
		text_matrix = [[cell.text.strip() for cell in col] for col in html_matrix]

		# Gets rid of empty cells
		filtered = [[cell for cell in col if cell != ''] for col in text_matrix]
		
		# Gets rid of empty rows
		filtered = [col for col in filtered if col]

		rows = iter(filtered)
		headers = [col for col in next(rows)]

		print headers
		for line in filtered:
			print len(line)#, line
			l = len(line)
			if l == 8:
				print 'Semester Summary', l, line
			elif l == 7:
				print 'Course', l, line
			elif l == 1:
				print 'Other', l, line
			elif l == 6:
				print 'Unknown', l, line
			#if len(line) == 1:
				


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