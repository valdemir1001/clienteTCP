import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!")
        print('Erro: {}'.format(e))
        sys.exit()
    print('Socket criado com sucesso!')


    hostAlvo = input('Digite o Host ou IP a ser conectado: ')
    portaAlvo = input('Digite a porta: ')

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print('Cliente CTP conectado com sucesso no Host: {} na Porta: {}'.format(hostAlvo,portaAlvo))
        s.shutdown(2)
    except socket.error as e:
        print('Não foi possivel conectar no Host: {} na Porta: {}'.format(hostAlvo, portaAlvo))
        print("Erro {}".format(e))
        sys.exit()

if __name__=='__main__':
    main()