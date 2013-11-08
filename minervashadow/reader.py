from HTMLParser import HTMLParser
from urlparse import urlparse
from urlparse import parse_qs
from bs4 import BeautifulSoup
import structures
import re

class MinervaReader:

	def __init__(self, site):
		self.s = site

	def welcomemsg(self, html):
		query = parse_qs(html.geturl())
		messg = HTMLParser().unescape(query['msg'][0])
		messg = messg.replace('<b>', '\n').replace('</b>', '\n')
		return messg

	def welcomeerr(self, html):
		# TODO:Instead we should try reading the error message displayed on the html
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

		def _is_semester_header(line):
			sem_header_regex = re.compile('^(Fall|Winter|Summer) ([0-9]{4})$')
			return sem_header_regex.match(line[0])

		def _is_standing(line):
			return line[0].startswith('Standing: ')

		def _is_education(line):
			return line[0].startswith('PREVIOUS EDUCATION ')

		def _is_description(line):
			return line[0].startswith('Bachelor of ')

		def _is_standing_header(line):
			return line[0] == 'Advanced Standing& Transfer Credits:'

		def _course_missing_avg(line):
			try:
				int(line[-1])
				return True
			except ValueError:
				return False

		def _course_missing_remarks(line):
			try:
				int(line[5])
				return True
			except ValueError:
				return False

		rows = iter(table)
		headers = [col for col in next(rows)]
		standing_headers = []

		print headers

		curriculum = structures.minervaCurriculum()

		for line in table:
			l = len(line)
			#print line
			if l == 1:
				if _is_semester_header(line):
					title = line[0].split(' ')
					sem = structures.minervaSemester(title[0],title[1])
					curriculum.addSemester(sem)
					print 'Added a semester.', sem

				elif _is_standing(line):
					curriculum.lastSemester().standing = line[0]
					#print curriculum.lastSemester().standing

				elif _is_education(line):
					education = re.sub('^PREVIOUS EDUCATION ', '', line[0])
					curriculum.education = education
					#print curriculum.education

				elif _is_description(line):
					description = re.sub('(\S[A-Z])', r' \1', line[0])
					curriculum.description = description
				else:
					#print l, 'Semester Name++', line
					pass

			elif l == 4:
				#print l, 'Exemption Ignored', line
				pass

			elif l == 5:
				if _is_standing_header(line):
					if not standing_headers:
						standing_headers = line
				else:
					print l, 'Unknown', line
					pass

			elif l == 6 or l == 7:
				if _course_missing_avg(line):
					line.append('')

				if _course_missing_remarks(line):
					line.insert(5, '')
				#print 'Added a course with missing info (6/8)'
				#courses = courses[-1].append(line)
				print len(line), line
				pass

			elif l == 8:
				pass# print l, 'TERM GPA', line
			elif l == 9:
				pass# print l, 'CUM GPA', line
			elif l == 23:
				pass# print l, 'Advanced Standing', line			
		print curriculum
