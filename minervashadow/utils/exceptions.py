"""
Global minervashadow exception and warning classes.
"""

class MinervaException(Exception):
	"""A generic exception for minervashadow."""
	pass
		

class NoInternetConnection(MinervaException):
	"""No internet connection has been detected."""
	pass


class AuthenticationRequired(MinervaException):
	"""You need to login to minerva before accessing this info."""
	pass