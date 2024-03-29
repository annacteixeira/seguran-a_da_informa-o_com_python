import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket criado com sucesso!')

host = 'localhost'
port = 5433
message = 'Olá, servidor!'

try:
    print('Cliente: ' + message)
    s.sendto(message.encode(), (host, 5432))

    data, server = s.recvfrom(4096)
    data = data.decode()
    print('Cliente: '+ data)

finally:
    print('Cliente: Fechando a conexão')
    s.close()

