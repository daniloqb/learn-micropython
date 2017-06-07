import socket
import sys

host = '192.168.6.117'
port = 55000

# FASE 1 : CRIA  O COMANDO

if len(sys.argv) == 4:                       # verifica os parametros
    gpio = str(sys.argv[1])                  # comando
    pin = str(sys.argv[2])                   # pino
    state = str(sys.argv[3])                 # stado
    cmd = gpio + ' ' + pin + ' ' + state     # monta o comando

    print (cmd)

    # FASE 2: CRIA A CONEXAO COM O SERVER

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria o socket
    s.connect((host,port))                                 # conecta ao server
    s.send(cmd.encode('utf8'))                             # envia o comando
    sRecv = s.recv(128)                                    # recebe do server
    s.close()                                              # fecha a conexao

    print('Recebido: ' +  sRecv.decode('utf8'))

