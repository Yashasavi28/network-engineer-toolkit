import socket

def whois_lookup(domain):

    s = socket.socket()

    s.connect(("whois.iana.org", 43))

    s.send((domain + "\r\n").encode())

    response = s.recv(4096).decode()

    s.close()

    return {
        "domain": domain,
        "whois": response
    }