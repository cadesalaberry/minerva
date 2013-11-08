class minervaSite:
	def __init__(self, _baseURL='https://horizon.mcgill.ca/pban1/'):
		self.base = _baseURL
		self.login = _baseURL + 'twbkwbis.P_ValLogin'
		self.logout = _baseURL + 'twbkwbis.P_Logout'
		self.search = _baseURL + 'bwckgens.p_proc_term_date'
		self.transcript = _baseURL + 'bzsktran.P_Display_Form?user_type=S&tran_type=V'
		self.quick_search = _baseURL + 'bwskfreg.P_AltPin'
		self.result = _baseURL + 'twbkwbis.P_Logout'


class minervaCred:
	def __init__(self, _mail, _password):
		self.usermail = _mail
		self.password = _password
		self.loggedin = False

	def __repr__(self):
		return '<Credentials of: %s>' % self.usermail


class minervaSemester:
	def __init__(self, _semester, _year):
		self.name = ' '.join((_semester, _year))
		self.year = _year
		self.classes = []
		self.semester = _semester
		self.standing = ''
		self.advanced = []
		self.description = ''

	def __repr__(self):
		return '<Semester: %s>' % self.name

	def add(self, course):
		self.semesters.append(course)


class minervaCurriculum:
	def __init__(self, _education='', _diploma=''):
		self.education = _education
		self.semesters = []
		self.diploma = _diploma
		
	def __repr__(self):
		return "<Curriculum: {0} ({1} semesters)>".format(self.diploma, len(self.semesters))

	def addSemester(self, semester):
		self.semesters.append(semester)

	def lastSemester(self):
		if not self.semesters:
			sem = minervaSemester('Empty','Semester')
			self.addSemester(sem)
		return self.semesters[-1]

def current_semester():

	return '201401'