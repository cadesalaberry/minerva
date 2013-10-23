import mechanize

class MinervaWriter:

	def __init__(self, site):
		self.s = site
		self.b = mechanize.Browser()

	def login(self, user):

		# Deals with the login page
		loginPage = self.b.open(self.s.login)
		self.b.select_form(name='loginform1')
		self.b["sid"] = user.usermail
		self.b["PIN"] = user.password

		return loginPage
