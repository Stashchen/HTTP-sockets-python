import socket
from view import index, pink

URLS = {
    '/': index,
    '/pink': pink,
    }

def parse_request(request):
    method, url, *args = request.split()
    return method, url

def generate_headers(method, url):
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if url not in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)

    return ('HTTP/1.1 200 OK\n\n', 200)

def generate_body(status_code, url):
    if status_code == 404:
        return '<h1>404</h1><p>Not found</p>'
    elif status_code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    else:
        return URLS[url]()

def generate_response(request):
    method, url = parse_request(request)
    header, status_code = generate_headers(method, url)
    body = generate_body(status_code, url)
    return (header + body).encode()

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(10)

    print('Starting server...')

    while True:
        conn, addr = server_socket.accept()

        request = conn.recv(1024)
        print('=' * 30)
        print('Client request:\n')
        print(request.decode('utf-8'))
        response = generate_response(request.decode('utf-8'))
        print('Server response:\n')
        print(response.decode('utf-8'))

        conn.sendall(response)
        conn.close()



if __name__ == "__main__":
    run()
