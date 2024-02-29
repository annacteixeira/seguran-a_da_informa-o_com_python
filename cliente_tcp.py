import socket, sys

def main():
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print("A conexão falhou.")
        print("Erro: {}".format(e))

        sys.exit()
    
    print("Socket criado com sucesso!")

    target_host = input("Digite o Host ou IP a ser conectado: ")
    target_port = input("Digite a porta a ser conectada: ")

    try:
        s.connect((target_host, int(target_port)))
        print("Cliente TCP conectado com sucesso no Host: " + target_host + " e na Porta: " + target_port)
        s.shutdown(2)
    
    except socket.error as e:
        print("A conexão falhou! Não foi possível conectar ao Host: " + target_host + " - Porta: " + target_port)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()