import mechanize

class MinervaSession:

	class minervaSite:
		def __init__(self):
			self.base = 'https://horizon.mcgill.ca/pban1/'
			self.login = self.base + 'twbkwbis.P_ValLogin'
			self.logout = self.base + 'twbkwbis.P_Logout'
			self.search = self.base + 'bwckgens.p_proc_term_date'
			self.quick_search = self.base + 'bwskfreg.P_AltPin'
			self.result = self.base + 'twbkwbis.P_Logout'


	class minervaCred:
		def __init__(self, _mail, _password):
			self.usermail = _mail
			self.password = _password


	def __init__(self, user):
		self.site = MinervaSession.minervaSite()
		self.user = MinervaSession.minervaCred(user[0],user[1])
		self.logged_in = False
		self.br = mechanize.Browser()


	def login(self) :
		br = self.br

		# Deals with the login page
		loginPage = br.open(self.site.login)
		br.select_form(name='loginform1')
		br["sid"] = self.user.usermail
		br["PIN"] = self.user.password

		# Logs in, This page can confirm a succesful login.
		loginResponse = br.submit()

		if loginResponse.geturl() == loginPage.geturl() :
			print 'Authorization Failure - you have entered an invalid McGill Username / Password.'
			print self.user.usermail
			exit()
		else:
			self.logged_in = True
			print loginResponse.geturl()

		return loginResponse.read()


	def logout(self):
		
		if not self.logged_in:
			print 'Please login first.'
			exit()

		# Logs out.
		logoutPage = self.br.open(self.site.logout)

		return logoutPage


	def deal_with_request(self, req):

		print req

		with open("response.html", "w") as webpage:
			if req['drop']:
				response = self.drop(req['<class_crn>'])

			else:
				print 'Not implemented yet.'

			webpage.write(response)


	def drop(self, crn):

		print 'Dropping', crn, '...'

		br = self.br

		# Selects the right semester on the semester page.
		br.open(self.site.quick_search)
		br.select_form(nr=1)
		br["term_in"] = '201309'

		dropPage = br.submit()

		print 'Class number', crn, 'dropped.'

		return dropPage.read()

