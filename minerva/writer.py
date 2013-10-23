import mechanize

class MinervaWriter:

	def __init__(self, site):
		self.site = site
		self.bwsr = mechanize.Browser()


	def login(self, user):

		# Deals with the login page
		loginPage = self.bwsr.open(self.site.login)

		self.bwsr.select_form(name='loginform1')
		self.bwsr["sid"] = user.usermail
		self.bwsr["PIN"] = user.password

		return self.bwsr.submit()


	def setsemester(self, semester):

		# Selects the right semester on the semester page.
		self.bwsr.open(self.site.quick_search)
		self.bwsr.select_form(nr=1)
		self.bwsr['term_in'] = semester

		return self.bwsr.submit()	


	def drop(self, crn):
		semester = ui.get_current_semester()

		print 'The class was not actually drop, missing implementation.'
		return self.setsemester(semester)


	def logout(self):

		# Logs out.
		logoutPage = self.bwsr.open(self.site.logout)

		return logoutPage
