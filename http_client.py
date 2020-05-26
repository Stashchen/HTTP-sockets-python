import socket

status_line = 'GET /{url} HTTP/1.1\n'

headers = [
    'Host: {host}',
    'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Fbrefox/76.0',
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language: en-US,en;q=0.5',
    'Accept-Encoding: gzip, deflate',
    'Connection: keep-alive',
    'Upgrade-Insecure-Requests: 1',
    'Cache-Control: max-age=0\n'
]


def get_server_name():
    name = input('Enter the address: ')
    if '/' not in name:
        name += '/'
    host_name, addr = name.split('/', 1)
    return socket.gethostbyname(host_name), host_name, addr

def run():
    ip, host_name, url = get_server_name()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.connect((ip, 8080))
    request = (status_line + '\n'.join(headers)).format(url=url, host=host_name)
    client_socket.send(request.encode())
    response = client_socket.recv(1024)
    print(response.decode('utf-8'))

if __name__ == "__main__":
    run()
