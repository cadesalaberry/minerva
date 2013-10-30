from HTMLParser import HTMLParser
from urlparse import urlparse
from urlparse import parse_qs
from bs4 import BeautifulSoup
import structures

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
		
		def _clean(cell):
			
			cell = cell.replace(u'\xa0', u'\n')
			cell = cell.strip()
			cell = ' '.join(cell.split())

			return cell

		def _clean_html_table(tbl):

			# Turns the html table into a list of lists (2D)
			html_matrix = [col.findAll('td') for col in tbl.findAll('tr')]

			# Gets rid of the html formatting to get only text
			text_matrix = [[_clean(cell.text) for cell in col] for col in html_matrix]

			# Gets rid of empty cells
			filtered = [[cell for cell in col if cell != ''] for col in text_matrix]
			
			# Gets rid of empty rows
			filtered = [col for col in filtered if col]
			
			return filtered



		soup = BeautifulSoup(html)

		# Gets the div containing the table
		div = soup.body.find('div', {'class':'pagebodydiv'})

		# Gets the table inside that div
		tbl = div.find('table', {'class':'dataentrytable', 'width':'100%'})
	
		table = _clean_html_table(tbl)

		print self._semesters_from_table(table)
		
		return True




	def _semesters_from_table(self, table):

		def is_semester_header(line):
			semesters = ('Fall', 'Winter', 'Summer')
			return any(semester in line for semester in semesters)

		rows = iter(table)
		headers = [col for col in next(rows)]

		print headers
		sizes = []
		courses = []
		for line in table:
			l = len(line)
			sizes.append(l)
			print l, line
			if l == 1:
				if is_semester_header(line):
					#print 'Added a semester.'
					courses = courses.append(line)
				pass
				# print l, 'Semester Name++', line
			elif l == 4:
				pass#print l, 'Unknown', line
			elif l == 5:
				pass#print l, 'Unknown', line
			elif l == 6:
				#print 'Added a course with missing info (6/8)'
				#courses = courses[-1].append(line)
				pass# print l, 'Course-', line
			elif l == 7:
				#print 'Added a course with missing info (7/8)'
				#courses = courses[-1].append(line)
				pass# print l, 'Course', line
			elif l == 8:
				pass# print l, 'TERM GPA', line
			elif l == 9:
				pass# print l, 'CUM GPA', line
			elif l == 23:
				pass# print l, 'Advanced Standing', line			
		print courses
		print list(set(sizes))
