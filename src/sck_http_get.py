#from __future__ import print_function

def http_get(url):
    import socket
    _,_,host,path = url.split('/',3)
    addr = socket.getaddrinfo(host,80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path,host),'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data,'utf8'), endl='')
        else:
            break
    s.close()



#http_get('http://www.fca.unicamp.br/portal')
