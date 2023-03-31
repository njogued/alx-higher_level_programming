### 0x11. Python - Network #1

#### Concepts
[Resource - The urllib Package](https://docs.python.org/3/howto/urllib2.html)

#### The urllib Package
- urllib.request fetches URLs using the ```urlopen``` function. The module can handle basic authentication, cookies, proxies, etc, and these functions are provided by handlers and openers.  
  
##### Fetching URLs
```
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
```
- urllib.request mirrors HTTP by sending requests and receiving responses. The response is a file-like object that can be read using the ```.read()``` function.
```
import urllib.request

req = urllib.request.Request('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
```
#### Passing data
- Data may be sent to a URL using a POST request. For HTML forms, the data has to be encoded (usually using the urllib.parse library) and then passed to the Request object as a data object, i.e.:

```
import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
```

- Without the data argument urllib uses a GET request. Data may also be passed to the GET request by encoding it in the URL.
```
import urllib.request
import urllib.parse
data = {}
data['name'] = 'Somebody Here'
data['location'] = 'Northampton'
data['language'] = 'Python'
url_values = urllib.parse.urlencode(data)
print(url_values)  # The order may differ from below.
name=Somebody+Here&language=Python&location=Northampton
url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_values
data = urllib.request.urlopen(full_url)
```
  
#### Modifying the HTTP header

