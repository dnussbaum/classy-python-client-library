# Classy API Python Client Library

##Description
I needed to interact with the Classy API but they didn't provide client libraries. This is a Python client I built to make those interactions a little easier.

**I have no affiliation with Classy.**

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
When using a response object as an iterator, the next page of results will automatically be requested as needed. 

```
import classyclient

client = classclient.ClassyClient([API KEY],[API SECRET])
activity = client.get("organizations/0123456/activity")

response.collection # True

for item in activity:
	print item['type']
```

###Updating Resources
```
import classyclient

client = classclient.ClassyClient([API KEY],[API SECRET])
response = client.put("campaign/0123456", data={"name":"new name"})
```
