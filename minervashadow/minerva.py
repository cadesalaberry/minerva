import utils.structures as structures
import utils.exceptions as exceptions
from writer import MinervaWriter
from reader import reader
import urllib2


def internet_needed(fn):
	def wrapper(*args, **kwargs):
		try:
			fn(*args, **kwargs)
		except urllib2.URLError as err:
			raise exceptions.NoInternetConnection
	return wrapper


def login_required(fn):
	def wrapper(self, *args, **kwargs):
		if not self.user.loggedin:
			raise exceptions.AuthenticationRequired
		fn(self, *args, **kwargs)
	return wrapper


class MinervaSession:

	def __init__(self, user):

		self.site = structures.minervaSite()
		self.user = structures.minervaCred(user[0],user[1])
		self.writer = MinervaWriter(self.site)
		self.reader = reader.MinervaReader(self.site)

	@internet_needed
	def login(self) :

		# Logs in, This page can confirm a succesful login.
		loginResponse = self.writer.login(self.user)

		loggedin, msg = self.reader.login(loginResponse)

		print msg[0]

		self.user.loggedin = loggedin

		return loginResponse.read()

	@internet_needed
	def logout(self):
		
		if not self.user.loggedin:
			print 'You are already logged out.'
		else:
			# Logs out.
			logoutPage = self.writer.logout()

		return logoutPage.read()

	@internet_needed
	@login_required
	def drop(self, crn):

		print 'Dropping', crn, '...'

		dropPage = self.writer.drop(crn)
		
		return dropPage.read()

	@internet_needed
	@login_required
	def transcript(self):

		transcriptPage = self.writer.transcript()
		
		curriculum = self.reader.transcript(transcriptPage)

		print str(curriculum)
		print curriculum.json()
		return curriculum

	@internet_needed
	@login_required
	def list(self):

		print 'Working on this function now.'

	@internet_needed
	def deal_with_request(self, req):

		with open("response.html", "w") as webpage:
			
			if req['login']:
				response = self.login()
			
			elif req['drop']:
				response = self.drop(req['<class_crn>'])

			elif req['transcript']:
				response = self.transcript()

			else:
				print 'Not implemented yet.'