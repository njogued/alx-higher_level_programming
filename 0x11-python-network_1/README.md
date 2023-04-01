### 0x11. Python - Network #1

#### Concepts
[Resource - The urllib Package](https://docs.python.org/3/howto/urllib2.html)  
[Resource - Requests](https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls)

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
- A dictionary of headers may be passed to the Request as a parameter
```
import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
```

#### Handling Exceptions
- Exception classes are found in the urllib.error module. Common errors are HTTP Error and URL Error.
```
req = urllib.request.Request('http://www.pretend_server.org')
try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)

(4, 'getaddrinfo failed')
HTTPError
```

#### Using Requests
- The request module can be used to GET, POST, PUT, DELETE, HEAD, etc as shown:
```
response = requests.get('https://api.github.com/events')
response = requests.post('https://httpbin.org/post', data={'key': 'value'})
response = requests.put('https://httpbin.org/put', data={'key': 'value'})
response = requests.delete('https://httpbin.org/delete')
response = requests.head('https://httpbin.org/get')
response = requests.options('https://httpbin.org/get')
```
- requests.get returns a response object. Methods that can be used with the response include: ```response.text``` - outputs text content, ```response.encoding``` - find out the encoding, and ```response.content``` that accesses the response body as bytes. 
- JSON response content may also be accessed by calling the ```.json``` on the response object.
- Parameters may also be passed to requests.get as key value pairs. For example:
```
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)

# OUTPUT: https://httpbin.org/get?key2=value2&key1=value1
```
- Custom headers can also be passed as key: value pairs
```
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
```
#### Handling exceptions
- ```Response.raise_for_status()``` checks for exception such as:
```
HTTPError if the request returned an unsuccessful status code
Timeout if a request times out
TooManyRedirects if a request exceeds the configured number of max redirects
```

#### Task 0. What's my status? #0
- Write a Python script that fetches https://alx-intranet.hbtn.io/status
```
You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
You must use a with statement
```
  
#### Task 1. Response header value #0
- Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
```
You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed to the script (number or type)
You must use a with statement
```
  
#### Task 2. POST an email #0
- Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
```
The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
```
  
#### Task 3. Error code #0
- Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
```
You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
```
  
#### Task 4. What's my status? #1
- Write a Python script that fetches https://alx-intranet.hbtn.io/status
```
You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)
```
  
#### Task 5. Response header value #1
- Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
```
You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You don’t need to check script arguments (number and type)
```
  
#### Task 6. POST an email #1
- Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
```
The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to error check arguments passed to the script (number or type)
```
  
#### Task 7. Error code #1
- Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
```
If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
```
  
#### Task 8. Search API
- Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
```
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
```
  
#### Task 9. My GitHub!
- Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
```
You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
```
  
#### Task 10. Time for an interview! (advanced)
- The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:
```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```
- Write a Python script that takes 2 arguments in order to solve this challenge.
```
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
```
