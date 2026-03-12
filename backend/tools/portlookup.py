PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    179: "BGP",
    25: "SMTP"
}

def port_lookup(port):

    service = PORTS.get(port, "Unknown")

    return {
        "port": port,
        "service": service
    }