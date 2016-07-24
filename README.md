# Classy API Python Client Library

##Description
**This project is still very much a work in progress. There is no guarantee that it will work properly.**

I need to interact extensively with the [Classy](classy.org) API ([docs here](https://developers.classy.org/api-docs/v2/index.html)) but they provide no client libraries. This is a Python client I built that makes interacting with their API a little easier.

I have no affiliation with Classy.

##Dependencies
- [Requests](http://docs.python-requests.org/en/master/): `pip install requests`

##Methods of ClassyClient
- **`get()`** with parameters:
	- **`endpoint:`** the endpoint for your request.
	- **`params:`** a dictionary of URL query string parameters. (opt.)
	- **`expand:`** a list of nested resources to expand. (opt.)
	- **`page:`** the page of the request to start on. The default is 1. (opt.)
	- **`per_page:`** the page size of the request. The Classy API default is 20. (opt.)  	

- **`post()`** with parameters:
	- **`endpoint:`** the endpoint for your request.
	- **`data:`** a dictionary of request body data. (opt.)

- **`put()`** with parameters:
	- **`endpoint:`** the endpoint for your request.
	- **`data:`** a dictionary of request body data.
	- **`params:`** a dictionary of URL query string parameters. (opt.)

- **`delete()`** with parameters:
	- **`endpoint:`** the endpoint for your request.

##Errors
If the API returns an error, a `ClassyResponseError` will be raised.

##Examples

###Fetching Resources
This is a call to get a specific fundraising page and expand the embedded 'fundraising_team' resource.

```
import classyclient

client = classclient.ClassyClient([API KEY],[API SECRET])
response = client.get("fundraising-pages/123456", expand=['fundraising_team'])
response.data # JSON object
```

###Fetching a Collection of Resources

```
import classyclient

client = classclient.ClassyClient([API KEY],[API SECRET])
response = client.get("organizations/0123456/activity")

response.collection # True

response.current_page # 1
response.data # First page's data
response.next_page() # True, if there is a next page
response.current_page # 2
response.data # Second page's data
```

###Updating Resources
```
import classyclient

client = classclient.ClassyClient([API KEY],[API SECRET])
response = client.put("campaign/0123456", data={"name":"new name"})
```
