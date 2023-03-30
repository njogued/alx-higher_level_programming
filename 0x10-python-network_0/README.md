## 0x10. Python - Network #0

### Concepts
[Resource](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
#### HTTP (HyperText Transfer Protocol)
- HTTP is an application layer (Layer #7) protocol [designed to transmit data between a webserver and the client](https://www.checkpoint.com/cyber-hub/network-security/what-is-the-osi-model-understanding-the-7-layers/#:~:text=The%20application%20layer%20includes%20protocols,web%20server%20and%20a%20client.)  
- [ChatGPT](https://chat.openai.com/chat): Imagine that the internet is like a vast library of information, and each web page is like a book in that library. HTTP is like the librarian who helps you find and retrieve the book you're looking for.  
- When a user tries to access a URL, the browser sends a HTTP request to the server hosting the web server. The server sends a HTTP response back with the page requested and other info necessary such as images, CSS, & JavaScript code.

#### HTTP Request Messages 
- The URL (Uniform Resource Locator), uniquely identifies a resource over the web. The URL has 4 parts: the protocol, hostname, port, path and file name.```protocol://hostname:port/path-and-file-name```
- The HTTP request message has: 
```
Request Line
Request Headers
<BLANK LINE>
Request Message Body (Optional)
```
- The request line is the first line of the header. The request line's syntax is ```request-method-name request-URI HTTP-version```
- The request header has name:value pairs with names such as Host, Accept, Accept-Language, Accept-Encoding, User-Agent, Content-Length
- The HTTP request message may then be:
```
GET / HTTP/1.1
Host: njogued.tech
User-Agent: curl/7.68.0
```
##### Request Methods
Request Methods include: GET, POST, PUT, DELETE, HEAD, DELETE, TRACE, OPTIONS, CONNECT, others  

#### HTTP Response Messages
- The HTTP response message has:
```
Status Line
Response Headers
<BLANK LINE>
Response Message Body (optional)
```
The status line: ```HTTP-version status-code reason-phrase```
The response header has name:value pairs with names such as Content-Type, Content-Length, Connection, and Keep-Alive. 
##### Status Codes - [Resource](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- Status codes are classified as:  
        100 - 199: Informational responses  
        200 - 299: Successful responses  
        300 - 399: Redirection messages  
        400 - 499: Client error responses  
        500 - 599: Server error responses  

- The HTTP response message may be:
```
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 30 Mar 2023 17:02:51 GMT
Content-Type: text/html
Content-Length: 13
Last-Modified: Tue, 28 Mar 2023 19:43:55 GMT
Connection: keep-alive
ETag: "6423437b-d"
Accept-Ranges: bytes
```

####
#### NOTE
- HTTP is stateless, ie. does not keep track of what has been done in the past.

### Task 0. cURL body size
- Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
```
The size must be displayed in bytes
You have to use curl
```
