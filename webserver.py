from http.server import BaseHTTPRequestHandler, HTTPServer
# from socketserver import TCPServer
import cgi

users = ['User-one', 'User-two']
# the class that will handle get and post requests 
class request_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/'):
            self.send_response(200)
            # setup the response headers
            self.send_header('content-type', 'text/html')
            # self.send_header('content-length', 100)
            self.end_headers()
            # content that will be sent along in the server's response
            response_content = '''
                <html>
                    <body>
                        <h3> List of users </h3>
                        <ul>
            '''
            for user in users:
                response_content += '<li>' + user + '</li>'

            response_content += '</ul>'
            response_content += '''
                        <p> Not yet a member? Click <a href="/visitor"> here </a> to join </p>
                    </body>
                </html>
            '''
            self.wfile.write(response_content.encode())


        # if a person navigates to the visitor form page
        if self.path.endswith('visitor'):
            self.send_response(200)
            # response headers
            self.send_header('content-type', 'text/html')
            # self.send_header('content-length', 100)
            self.end_headers()
            # response content
            response_content = '''
                <html>
                    <body>
                        <h3>Join our list of users!</h3>
                        <form action="/visitor" method="post" enctype="multipart/form-data">
                            <input type="text" name="name" placeholder="Enter your name here" required>
                            <input type="submit" value="Join">
                        </form>
                    </body>
                </html>
            '''
            self.wfile.write(response_content.encode())


    # for post requests submitted through the visitor form created earlier
    def do_POST(self):
        if self.path.endswith('visitor'):
            # use the cgi module to determine the visitor form content type
            content_type, values_dict = cgi.parse_header(self.headers.get('content-type'))
            content_length = int(self.headers.get('Content-length'))
            values_dict['boundary'] = bytes(values_dict['boundary'], "utf-8")
            values_dict['CONTENT-LENGTH'] = content_length
            if content_type == 'multipart/form-data':
                # save the form fields as key-value pairs in the values_dict created earlier
                form_fields = cgi.parse_multipart(self.rfile, values_dict)
                visitor_name = form_fields.get('name')
                users.append(str(visitor_name)[2:-2])

            # redirect to the root url after a successful post action
            self.send_response(301)
            self.send_header('content-type', 'text/html')
            # specify the redirect location
            self.send_header('location', '/')
            self.end_headers()


def main():
    # define the port the server will listen on
    PORT = 4735
    # bind the server to the defined host, port, and call the request handler
    server = HTTPServer(('', PORT), request_handler)
    print("Web server started at http://localhost:{}".format(PORT))
    server.serve_forever()
    


# to ensure the main function runs whenever this(webserver.py) file gets run;
if __name__ == '__main__':
    main()