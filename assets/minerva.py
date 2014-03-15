import sys
import cgi
import cgitb
import getpass
import mechanize
from bs4 import BeautifulSoup
from Queue import Queue

class MinervaSession:

	class minervaSite:
		def __init__(self, _base_url):
			self.base = _base_url
			self.login = self.base + 'twbkwbis.P_ValLogin'
			self.logout = self.base + 'twbkwbis.P_Logout'
			self.search = self.base + 'bwckgens.p_proc_term_date'
			self.quick_search = self.base + 'bwskfreg.P_AltPin'
			self.result = self.base + 'twbkwbis.P_Logout'

	class minervaUser:
		def __init__(self, _mail, _password):
			self.usermail = _mail
			self.password = _password
			self.crn_list = Queue(10)
			self.semester = '201305'
			self.result = ''

	def __init__(self):
		self.site = MinervaSession.minervaSite('https://horizon.mcgill.ca/pban1/')
		self.user = False
		self.logged_in = False
		self.br = mechanize.Browser()

	# Reads the user input from the user or raw stdin
	def get_user_input(self):

		_param = Queue(14)
		#################################################
		# Gets the user credential to store in the user #
		#################################################
		if sys.stdin.isatty():
			# Gets the credentials from the user
			_mail = raw_input('Email? ')
			_pin = getpass.getpass(stream=sys.stderr)

		else:
			# Gets the credentials from stdin
			for arg in sys.stdin.readlines():
				_param.put(arg)

			if _param.qsize() < 3:
				print 'Error: Malformed input. Missing arguments.'
				exit()

			else:
				_mail = _param.get().strip()
				_pin = _param.get().strip()
				

		_user = MinervaSession.minervaUser(_mail, _pin)

		######################################
		# Gets the CRNs to store in the user #
		######################################
		if sys.stdin.isatty():
			# Gets the CRNs from the user
			while not _user.crn_list.full():

				_tempCRN = raw_input('CRN? ')
				
				if _tempCRN.isdigit() :
					_user.crn_list.put(_tempCRN)
				else :
					break
		else:
			# Gets the CRNs from stdin
			while not _user.crn_list.full() and not _param.empty() :
				_user.crn_list.put(_param.get().strip())

		form = cgi.FieldStorage()
		if "usermail" in form :
			print 'form!!!'



		self.user = _user
		return _user

	def login(self) :
		#print 'Logging in...'
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
			#print loginResponse.geturl()

	def logout(self):
		
		if not self.logged_in:
			print 'Please login first.'
			exit()

		# Logs out.
		logoutPage = self.br.open(self.site.logout)

	

	# Returns a mechanize page of submission result
	def set_semester(self, semester):

		if not self.logged_in:
			print 'Please login first.', self.logged_in
			exit()
		else:
			br = self.br
		# Goes to the Quick Add page.
		br.open(site.quick_search)

		# Selects the right semester.
		br.select_form(nr=1)
		br["term_in"] = [semester]

		return br.submit()

	def get_registration_status(self, submitPage):
		bs = BeautifulSoup(submitPage.read())

		return bs.find( "table", {"class":"datadisplaytable"} )

	def register_crns(self):

		if not self.logged_in:
			print 'Error: Register: Hey', self.logged_in, 'please login first.'
			exit()
		else:
			_crns = self.user.crn_list
			br = self.br

		# Selects the right semester on the semester page.
		br.open(self.site.quick_search)
		br.select_form(nr=1)
		br["term_in"] = [self.user.semester]
		br.submit()

		# Selects the right form.
		br.select_form(nr=1)
		# Allows to edit hidden fields.
		br.set_all_readonly(False)
		#for form in br.forms() :
		#	print form.name
		#	for control in form :
		#		print '\t', control

		#forms = ParseResponse(quickAddPage, backwards_compat=False)
		#form = forms[1]
		
		# Sets values according to Minerva HTML code.
		for control in br.controls :
			
			#print control.name
			_old = control.value

			if control.name == 'CRN_IN' :
				if not _crns.empty() :
					# Sets Desired CRNs.
					control.value = _crns.get()
					#print 'Registering for CRN', control.value
				else :
					break
			
			if control.name == 'assoc_term_in' : control.value = ''
			if control.name == 'start_date_in' : control.value = ''
			if control.name == 'end_date_in' : control.value = ''
			if control.name == 'RSTS_IN' :
				try: control.value = 'RW'
				except TypeError: control.value[0] = 'RW'

			#print '\t', _old, "\t >", control.value

		# Submits registration request for the specified CRN.
		self.result = self.get_registration_status(br.submit())
		return self.result


session = MinervaSession()
session.get_user_input()
#session.login()

#print session.register_crns()

#session.logout()