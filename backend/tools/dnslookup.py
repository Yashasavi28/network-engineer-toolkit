import socket

def dns_lookup(domain):

    try:

        ip = socket.gethostbyname(domain)

        return {
            "domain": domain,
            "ip": ip
        }

    except:

        return {"error": "DNS lookup failed"}