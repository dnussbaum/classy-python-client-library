# Classy API Python Client Library

## Description

I needed to interact with the Classy API but they didn't provide a client library in Python. This is a Python client I built to make those interactions a little easier.

_I have no affiliation with Classy._

## Installation

Install with **pip**.

```bash
pip install classyclient
```

## Methods of ClassyClient

- **`get()`** with parameters:

  - **`endpoint:`** the endpoint for your request.
  - **`expand:`** a list of nested resources to expand. (opt.)
  - **`page:`** the page of the request to start on. Default is 1\. (opt.)
  - **`per_page:`** the page size of the request. Default is 20\. (opt.)
  - Additional parameters can be passed as keyword arguments.

- **`post()`** with parameters:

  - **`endpoint:`** the endpoint for your request.
  - Data for the request body can be passed with keyword arguments.

- **`put()`** with parameters:

  - **`endpoint:`** the endpoint for your request.
  - **`data:`** a dictionary of request body data.
  - Additional parameters can be passed as keyword arguments.

- **`delete()`** with parameters:

  - **`endpoint:`** the endpoint for your request.

## Errors

If the API returns an error, a `ClassyResponseError` will be raised.

## Examples

### Fetching Resources

This is a call to get a specific fundraising page and expand the embedded `fundraising_team` resource.

```python
import classyclient

client = classyclient.ClassyClient(API_KEY, API_SECRET)
response = client.get("fundraising-pages/123456", expand=["fundraising_team"])
response.data # Python dictionary
str(response) # JSON string
```

### Fetching a Collection of Resources

When using a response object as an iterator, the next page of results will automatically be requested as needed.

```python
import classyclient

client = classyclient.ClassyClient(API_KEY, API_SECRET)
activity = client.get("organizations/0123456/activity")

response.collection # True

for item in activity:
    print item["type"]
```

### Updating Resources

```python
import classyclient

client = classclient.ClassyClient([API KEY], [API SECRET])
response = client.put("campaign/0123456", data={"name":"new name"})
```
