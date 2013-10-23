class minervaSite:
	def __init__(self):
		self.base = 'https://horizon.mcgill.ca/pban1/'
		self.login = self.base + 'twbkwbis.P_ValLogin'
		self.logout = self.base + 'twbkwbis.P_Logout'
		self.search = self.base + 'bwckgens.p_proc_term_date'
		self.transcript = self.base + 'bzsktran.P_Display_Form?user_type=S&tran_type=V'
		self.quick_search = self.base + 'bwskfreg.P_AltPin'
		self.result = self.base + 'twbkwbis.P_Logout'


class minervaCred:
	def __init__(self, _mail, _password):
		self.usermail = _mail
		self.password = _password
		self.loggedin = False


def currentsemester():

	return '201401'