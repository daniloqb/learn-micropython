import machine
import network
import time
import socket

ssid = 'CASA_NETWORK'
passwd = '8fc51f82x2'

host = '0.0.0.0'
port = 55000


# FASE 1 -- CONECTA-SE A REDE WIFI

# interfaces de rede

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

# desativa a interface AP
ap_if.active(False)

# tenta se conectar ao router

print('Connecting...')
if not sta_if.isconnected():       # se ainda nao estiver conectado
    sta_if.active(True)            # ativa a interface
    sta_if.connect(ssid, passwd)   # conecta se com o ssid e o passwd

print(sta_if.ifconfig())


# espera um tempo antes de abrir o socket.
time.sleep(2)


# FASE 2 --  CRIA O SERVIDOR PARA RECEBER REQUISIÇÕES

print ('Initializing Server...')
# create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind na porta
server.bind((host,port))

# comeca a ouvir na porta
server.listen(5)

# FASE 3 -- OUVE AS REQUISICOES

while True:                                       # loop eterno
    client, add = server.accept()                 # cria um socket para um cliente conectado
    print ('New client')
    sRecv = client.recv(128)                      # pega 128 bytes enviados pelo cliente
    sAscii = sRecv.decode('utf8')                 # decodifica para utf8
    sParam = sAscii.split(' ')                    # divide a string recebida
    if sParam[0] == 'GPOUT':                      # comando: GPOUT 2 1
        pin = int(sParam[1])                      # segundo parametro eh o pino
        val = int(sParam[2])                      # terceiro parametro eh o valor do pino
        led = machine.Pin(pin,machine.Pin.OUT)    # configura o pino
        led.value(val)                            # configura o valor do pino

    # devolve ao cliente o mesmo dado recebido
    client.send(sRecv)

    # fecha a conexao
    client.close()
    print ('Closing connection')





