from writer import MinervaWriter
from reader import MinervaReader
import structures

class MinervaSession:

	def __init__(self, user):

		self.site = structures.minervaSite()
		self.user = structures.minervaCred(user[0],user[1])
		self.writer = MinervaWriter(self.site)
		self.reader = MinervaReader(self.site)


	def login(self) :

		# Logs in, This page can confirm a succesful login.
		loginResponse = self.writer.login(self.user)

		if loginResponse.geturl() == self.site.login:
			print self.reader.welcomeerr(loginResponse)
			exit()
		
		self.user.loggedin = True
		print self.reader.welcomemsg(loginResponse)

		return loginResponse.read()


	def logout(self):
		
		if not self.user.loggedin:
			print 'Please login first.'
			exit()

		# Logs out.
		logoutPage = self.writer.logout()

		return logoutPage.read()


	def drop(self, crn):

		print 'Dropping', crn, '...'

		dropPage = self.writer.drop(crn)
		
		return dropPage.read()


	def list(self):

		print 'Working on this function now.'


	def deal_with_request(self, req):

		#print req

		with open("response.html", "w") as webpage:
			if req['login']:
				response = self.login()
			elif req['drop']:
				response = self.drop(req['<class_crn>'])

			else:
				print 'Not implemented yet.'

			webpage.write(response)