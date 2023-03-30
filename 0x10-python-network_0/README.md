## 0x10. Python - Network #0

### Concepts
#### HTTP (HyperText Transfer Protocol)
- HTTP is an application layer (Layer #7) protocol [designed to transmit data between a webserver and the client](https://www.checkpoint.com/cyber-hub/network-security/what-is-the-osi-model-understanding-the-7-layers/#:~:text=The%20application%20layer%20includes%20protocols,web%20server%20and%20a%20client.)  
- ChatGPT: Imagine that the internet is like a vast library of information, and each web page is like a book in that library. HTTP is like the librarian who helps you find and retrieve the book you're looking for.  
- When a user tries to access a URL, the browser sends a HTTP request to the server hosting the web server. The server sends a HTTP response back with the page requested and other info necessary such as images, CSS, & JavaScript code.
- The URL (Uniform Resource Locator), uniquely identifies a resource over the web. The URL has 4 parts: the protocol, hostname, port, path and file name.```protocol://hostname:port/path-and-file-name```
- The HTTP request message may then be:
```
GET path-and-file-name HTTP/1.1
Host: hostname
Accept: image/gif
User-Agent: Mozilla/4.0
```

- The HTTP response message may be:
```
HTTP/1.1 200 OK
Date: Thur, 30 Mar 2023
Server: Nginx

#### NOTE
- HTTP is stateless, ie. does not keep track of what has been done in the past.

### Task 0. cURL body size
- Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
```
The size must be displayed in bytes
You have to use curl
```
