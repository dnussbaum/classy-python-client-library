from Exceptions import *

class ClassyClientResponse:
	"""Returned after an API request by ClassyClient. Allows for paging of results."""

	def __init__(self, response, session):
		self.total = None
		self.per_page = None
		self.last_page = None
		self.current_page = None
		self.__response = response
		self.__session = session
		self.__refresh()

	def __refresh(self):
		"""Refresh the ClassyClientResponse object after paging."""
		json = self.__response.json()

		if "total" in json:
			self.collection = True
			self.total = json['total']
			self.per_page = json['per_page']
			self.current_page = json['current_page']
			self.last_page = json['last_page']
			self.data = json['data']
			self.__next_page_url = json['next_page_url']
			self.__prev_page_url = json['prev_page_url']
		else:
			self.collection = False
			self.data = json

	def next_page(self):
		"""
		Get the next page of results.
		Returns True on success, False is there isn't a next page.
		"""
		if not self.collection:
			raise ClassyRequestError("Not a collection")
		if self.current_page is self.last_page:
			return False

		self.__response.request.url = self.__next_page_url
		self.__response = self.__session.send(self.__response.request)
		self.__refresh()
		return True

	def previous_page(self):
		"""
		Get the previous page of results.
		Returns True on success, False is there isn't a previous page.
		"""
		if not self.collection:
			raise ClassyRequestError("Not a collection")
		if self.current_page is 1:
			return False

		self.__response.request.url = self.__prev_page_url
		self.__response = self.__session.send(self.__response.request)
		self.__refresh()
		return True
