import utils.structures as structures
from writer import MinervaWriter
from reader import reader

class MinervaSession:

	def __init__(self, user):

		self.site = structures.minervaSite()
		self.user = structures.minervaCred(user[0],user[1])
		self.writer = MinervaWriter(self.site)
		self.reader = reader.MinervaReader(self.site)


	def login(self) :

		# Logs in, This page can confirm a succesful login.
		loginResponse = self.writer.login(self.user)

		print self.reader.login(loginResponse)

		if loginResponse.geturl() != self.site.login:
			self.user.loggedin = True
		else:
			self.user.loggedin = False

		return loginResponse.read()


	def logout(self):
		
		if not self.user.loggedin:
			print 'You are already logged out.'
		else:
			# Logs out.
			logoutPage = self.writer.logout()

		return logoutPage.read()


	def drop(self, crn):

		print 'Dropping', crn, '...'

		dropPage = self.writer.drop(crn)
		
		return dropPage.read()


	def transcript(self):

		transcriptPage = self.writer.transcript()
		
		curriculum = self.reader.transcript(transcriptPage)

		print curriculum

		return curriculum

	def list(self):

		print 'Working on this function now.'


	def deal_with_request(self, req):

		#print req

		with open("response.html", "w") as webpage:
			
			if req['login']:
				response = self.login()
			
			elif req['drop']:
				response = self.drop(req['<class_crn>'])

			elif req['transcript']:
				response = self.transcript()

			else:
				print 'Not implemented yet.'

			#webpage.write(response)