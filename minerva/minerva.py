import mechanize
import structures
from writer import MinervaWriter
from reader import MinervaReader
import ui

class MinervaSession:

	def __init__(self, user):
		self.site = structures.minervaSite()
		self.user = structures.minervaCred(user[0],user[1])
		self.br = mechanize.Browser()
		self.writer = MinervaWriter(self.site)
		self.reader = MinervaReader(self.site)


	def login(self) :

		# Logs in, This page can confirm a succesful login.
		loginResponse = self.writer.login(self.user)

		if loginResponse.geturl() == loginPage.geturl() :
			print '\n\nAuthorization Failure - you have entered an invalid McGill Username / Password.'
			exit()
		else:
			self.user.loggedin = True
			print self.reader.welcomemsg(loginResponse)

		return loginResponse.read()


	def logout(self):
		
		if not self.user.loggedin:
			print 'Please login first.'
			exit()

		# Logs out.
		logoutPage = self.br.open(self.site.logout)

		return logoutPage


	def drop(self, crn):

		print 'Dropping', crn, '...'

		br = self.br

		# Selects the right semester on the semester page.
		br.open(self.site.quick_search)
		br.select_form(nr=1)
		br["term_in"] = ui.get_current_semester()

		dropPage = br.submit()

		print 'Class number', crn, 'dropped.'

		return dropPage.read()


	def list(self):

		print 'Working on this function now.'



	def deal_with_request(self, req):

		print req

		with open("response.html", "w") as webpage:
			if req['drop']:
				response = self.drop(req['<class_crn>'])

			else:
				print 'Not implemented yet.'

			webpage.write(response)