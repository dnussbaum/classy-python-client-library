import requests
import json
from ClassyClientResponse import ClassyClientResponse
from Exceptions import *

class ClassyClient:
	"""Classy Client Library."""

	URL_BASE = "https://api.classy.org/2.0/"

	def __init__(self, client_id, client_secret):
		self.__client_id = client_id
		self.__client_secret = client_secret
		self.__access_token = self.__generate_token()
		self.__session = requests.Session()

	def __generate_token(self):
		"""
		Get a Classy API OAuth token.
		See: https://developers.classy.org/overview/authentication
		"""
		response = requests.post("https://api.classy.org/oauth2/auth", params={
			"grant_type": "client_credentials",
			"client_id": self.__client_id,
			"client_secret": self.__client_secret
		}).json()

		if 'error' in response:
			raise ClassyAuthError("Invalid API key or secret")

		return response['access_token']

	def __call(self, method, endpoint, params={}, data={}, expand=[], page=None, per_page=None):
		"""Make a request."""
		headers = {'Authorization': "Bearer " + self.__access_token}

		endpoint = endpoint.strip("/")

		if expand:
			params.update({"with":",".join(expand)})

		if page:
			params.update({"page": page})

		if per_page:
			params.update({"per_page": per_page})

		r = self.__session.request(method, ClassyClient.URL_BASE + endpoint, params=params, json=data, headers=headers)

		if r.status_code is not requests.codes.ok:
			self.handle_error(r)

		return ClassyClientResponse(r, self.__session)

	def get(self, endpoint, params={}, expand=[], page=None, per_page=None):
		"""Make a GET request."""
		return self.__call("GET", endpoint, params=params, expand=expand, page=page, per_page=per_page)

	def post(self, endpoint, data={}):
		"""Make a POST request."""
		return self.__call("POST", endpoint, data=data)

	def put(self, endpoint, data, params={}):
		"""Make a PUT request."""
		return self.__call("PUT", endpoint, params=params, data=data)

	def delete(self, endpoint):
		"""Make a DELETE request."""
		return self.__call("DELETE", endpoint, params=params, data=data)

	def handle_error(self, response):
		"""Handle Classy errors."""
		error = response.json()['error']
		raise ClassyResponseError(error)
