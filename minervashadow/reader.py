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
		sizes = []
		courses = []
		for line in filtered:
			l = len(line)
			sizes.append(l)
			print l, line
			if l == 1:
				if 'Fall' in line or 'Winter' in line or 'Summer' in line:
					print 'Added a semester.'
					courses = courses.append(line)
				pass
				# print l, 'Semester Name++', line
			elif l == 4:
				pass#print l, 'Unknown', line
			elif l == 5:
				pass#print l, 'Unknown', line
			elif l == 6:
				print 'Added a course with missing info (6/8)'
				courses = courses[-1].append(line)
				pass# print l, 'Course-', line
			elif l == 7:
				print 'Added a course with missing info (7/8)'
				courses = courses[-1].append(line)
				pass# print l, 'Course', line
			elif l == 8:
				pass# print l, 'TERM GPA', line
			elif l == 9:
				pass# print l, 'CUM GPA', line
			elif l == 23:
				pass# print l, 'Advanced Standing', line			
		print courses
		print list(set(sizes))	


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