try:
    import usocket as socket
except:
    import socket


def main(use_stream = True):
    s = socket.socket()

    ai = socket.getaddrinfo("www.w3schools.com",80)
    print ("Address infos:", ai)
    addr = ai[0][-1]

    print ("Connect address", addr)
    s.connect(addr)

    if use_stream:
        # MicroPython socket objects support stream (aka file) interface
        # directly, but the line below is needed for CPython.
        s = s.makefile("rwb",0)
        s.write("GET / HTTP/1.0\r\n\r\n")
        while True:
            chunck = s.read(1024)
            if not len(chunck) > 0:
                break
            else:
                print(chunck)
    else:
        s.send("GET / HTTP/1.0\r\n\r\n")
        print(s.recv(4096))

    s.close()


main()