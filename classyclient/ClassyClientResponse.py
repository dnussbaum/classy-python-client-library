import json
from Exceptions import *

class ClassyClientResponse:
    """Returned after an API request by ClassyClient. Allows for paging of results."""

    def __init__(self, response, session):
        self.total = None
        self.per_page = None
        self.last_page = None
        self.current_page = None
        self.__response = response
        print self.__response.url
        self.__session = session
        self.__refresh()

    def __refresh(self):
        """Refresh the ClassyClientResponse object after paging."""
        json = self.__response.json()

        if "total" in json:
            self.collection = True
            self.total = json["total"]
            self.per_page = json["per_page"]
            self.current_page = json["current_page"]
            self.last_page = json["last_page"]
            self.data = json["data"]
            self.__next_page_url = json["next_page_url"]
            self.__prev_page_url = json["prev_page_url"]
            self.cursor = 0
        else:
            self.collection = False
            self.data = json

    def __str__(self):
        return json.dumps(self.data)

    def __len__(self):
        """Return the length of the result"""
        if self.collection:
            return self.total
        raise ClassyNotACollection("Not a collection")

    def __iter__(self):
        return self

    def next(self):
        """Get the next item. Handles paging when needed."""
        if not self.collection:
            raise ClassyNotACollection("Not a collection")

        if self.cursor < len(self.data):
            item = self.data[self.cursor]
            self.cursor += 1
            return item

        if self.next_page():
            self.cursor = 0
            item = self.data[self.cursor]
            self.cursor += 1
            return item
        else:
            raise StopIteration

    def next_page(self):
        """
        Get the next page of results.
        Returns True on success, False is there isn't a next page.
        """
        if not self.collection:
            raise ClassyNotACollection("Not a collection")

        if self.current_page is self.last_page or not self.__next_page_url:
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
            raise ClassyNotACollection("Not a collection")

        if self.current_page is 1 or not self.__previous_page_url:
            return False

        self.__response.request.url = self.__prev_page_url
        self.__response = self.__session.send(self.__response.request)
        self.__refresh()
        return True
