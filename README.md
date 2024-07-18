# Python HTTP Server

This is a simple HTTP server implemented from scratch using Python 3.12.4. The server can handle various HTTP requests, including GET, POST, and handling files.

## Features

1. **Basic HTTP Server**: The server listens on `localhost:4221` and responds with a basic "Hello" message for the root path (`/`).
2. **Echo Server**: The server can echo the path after `/echo/` in the response.
3. **User-Agent**: The server can display the user-agent information of the client in the response.
4. **File Server**: The server can serve files from a specified directory. It supports GET and POST requests for files.
   - GET requests will return the file content.
   - POST requests will save the request body to the specified file.

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/jxkx1/py-http-server.git
   ```

2. Change to the project directory:

   ```
   cd py-http-server
   ```

3. Run the server:

   ```
   python server.py <directory>
   ```

   Replace `<directory>` with the path to the directory you want the server to serve files from.

4. The server will start running on `localhost:4221`. You can test the server using the following commands:

   - Root path: `curl http://localhost:4221/`
   - Echo server: `curl http://localhost:4221/echo/hello`
   - User-agent: `curl http://localhost:4221/user-agent`
   - File server:
     - GET: `curl http://localhost:4221/files/example.txt`
     - POST: `curl -X POST -d "This is a sample file." http://localhost:4221/files/example.txt`

## Blog Post

I have written a blog post about the process of building this HTTP server from scratch using Python. You can read the post at the following link:

[Python HTTP Server - jxkxl's Blog](https://jxkx1.github.io/2024/07/18/python-http-server/)

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.