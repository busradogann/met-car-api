import requests

class Client():
	def __init__(self, url):
		print('x.Client init oldu')
		self.url = url

	def make_request(self):
		print('x.make_request init oldu')
		return requests.get(self.url)