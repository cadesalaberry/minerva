from HTMLParser import HTMLParser
from urlparse import urlparse
from urlparse import parse_qs
from bs4 import BeautifulSoup

class MinervaReader:

	def __init__(self, site):
		self.s = site

	def welcomemsg(html):

		query = parse_qs(html.geturl())
		messageHTML = '\n\n' + query['msg'][0]
		return HTMLParser().unescape(messageHTML)