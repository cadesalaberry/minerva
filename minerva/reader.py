from HTMLParser import HTMLParser
from urlparse import urlparse
from urlparse import parse_qs
from bs4 import BeautifulSoup

class MinervaReader:

	def __init__(self, site):
		self.s = site

	def welcomemsg(self, html):
		query = parse_qs(html.geturl())
		messg = HTMLParser().unescape(query['msg'][0])
		messg = messg.replace('<b>', '\n').replace('</b>', '\n')
		return messg

	def welcomeerr(self, html):
		# Instead we should try reading the error message displayed on the html
		return 'Authorization Failure - you have entered an invalid McGill Username / Password.'