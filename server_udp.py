import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso!')

host = 'localhost'
port = 5432

s.bind((host,port))
message = 'Servidor: Olá, cliente!'

while 1:
    data, adress = s.recvfrom(4096)

    if data:
        print('Servidor enviando mensagem...')
        s.sendto(data + (message.encode(), end))