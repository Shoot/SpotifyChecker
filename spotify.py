import json
import base64
import logging
import requests

class Checker:
	def __init__(self):
		# Initialize logger
		self.logger = logging.getLogger(__name__)

		# Initialize the session
		self.session = requests.Session()
		self.logger.info('Initialized the session')

		# Get the cookies
		resp = self.session.get("https://accounts.spotify.com/en/login/")
		self._get_bon(resp)
		self.logger.info('Got the `__bon` value and cookies')

	def _get_bon(self, resp):
		# Get the `BON` value and process it to make the `__bon` cookie
		# https://spotifylib.readthedocs.io/en/latest/_modules/spotifylib/spotifylib.html
		bon = json.loads(resp.text.split("sp-bootstrap-data='")[-1].split("'>")[0]).get('BON', [])
		bon.extend([bon[-1] * 42, 1, 1, 1, 1])

		# Set the cookie
		self.session.cookies['__bon'] = base64.b64encode(bytes('|'.join([str(entry) for entry in bon]), 'ascii')).decode('utf-8')

	def check(self, username, password):
		payload = {
			"remember": False,
			"username": username,
			"password": password,
			"csrf_token": self.session.cookies['csrf_token']
		}

		return self.session.post("https://accounts.spotify.com/api/login", data=payload).status_code == 200