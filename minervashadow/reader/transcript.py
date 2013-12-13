from ..utils import structures
import re

def _clean_cell(cell):
		
	cell = cell.replace(u'\xa0', u'\n') # Removes weird characters
	cell = cell.replace(u'\xb2', u'') # Removes the pow(2) character
	#cell = cell.strip().encode('utf8')	# Removes trailing spaces
	cell = ' '.join(cell.split())		# Removes useless '\n'

	return cell


def _clean_html_table(tbl):

	# Gets rid of the html formatting to get only text
	text_matrix = [[_clean_cell(cell.text) for cell in col] for col in tbl]

	# Gets rid of empty cells
	filtered = [[cell for cell in col if cell != ''] for col in text_matrix]
	
	# Gets rid of empty rows
	filtered = [col for col in filtered if col]
	
	return filtered


def _curriculum_from_table(table):

	def _is_semester_header(line):
		sem_header_regex = re.compile('^(Readmitted|)(Fall|Winter|Summer) ([0-9]{4})$')
		return sem_header_regex.match(line[0])

	def _is_standing(line):
		return line[0].startswith('Standing: ')

	def _is_education(line):
		return line[0].startswith('PREVIOUS EDUCATION ')

	def _is_description(line):
		return line[0].startswith('Bachelor of ')

	def _is_standing_header(line):
		return line[0] == 'Advanced Standing& Transfer Credits:'

	def _is_a_grade(text):
		rule = '^(A-|B+|B|B-|C+|C|D|F'
		rule += '|HH|IP|JK|KE|K\*|KF|KK|LL|LE|L\*'
		rule += 'NA|&&|NE|NR|P|Q|R|S|U|W|WF|WL|W--|--)$'

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

	def _course_missing_credits(line):
		
		_is_an_int = False

		for field in line[5:]:
			_is_an_int = field.isdigit()
			if _is_an_int:
				return True
		return False

	def _course_from_line(line):

		_course = structures.minervaCourse(line[0])
		
		if not len(line) is 8:
			return _course

		_course.number	= line[1]
		_course.title	= line[2]
		_course.credits	= line[3]
		_course.grade	= line[4]
		_course.remarks	= line[5]
		_course.earned	= line[6]
		_course.average = line[7]

		return _course


	rows = iter(table)
	headers = [col for col in next(rows)]
	standing_headers = []

	print headers

	curriculum = structures.minervaCurriculum()

	for line in table:
		l = len(line)

		if l == 1:
			if _is_semester_header(line):
				# Gets rid of the Readmitted word before the semester.
				title = re.sub('^Readmitted', '', line[0]).split(' ')
				sem = structures.minervaSemester(title[0],title[1])
				
				curriculum.addSemester(sem)

			elif _is_standing(line):
				curriculum.lastSemester().standing = line[0]

			elif _is_education(line):
				education = re.sub('^PREVIOUS EDUCATION ', '', line[0])
				curriculum.education = education

			elif _is_description(line):
				# Puts spaces before capital letters.
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
				# Credits transfer and course equivalence
				#print l, 'Unknown', line
				pass

		elif l == 6 or l == 7:
			if _course_missing_avg(line):
				line.append('')

			if _course_missing_remarks(line):
				line.insert(5, '')
			#print 'Added a course with missing info (6/8)'
			#courses = courses[-1].append(line)
			if len(line) is 8:
				_course = _course_from_line(line)
				curriculum.lastSemester().addCourse(_course)
			else:
				print line

		elif l == 8:
			pass# print l, 'TERM GPA', line
		elif l == 9:
			pass# print l, 'CUM GPA', line
		elif l == 23:
			pass# print l, 'Advanced Standing', line			
	
	print curriculum
	for semester in curriculum.semesters:
		print ' ', semester
		for course in semester.courses:
			print '  ', course

def get_curriculum(table):

	table = _clean_html_table(table)

	return _curriculum_from_table(table)
