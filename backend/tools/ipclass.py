def detect_ip_class(ip):

    first = int(ip.split(".")[0])

    if first <= 127:
        ip_class = "A"
        ip_range = "0.0.0.0 - 127.255.255.255"

    elif first <= 191:
        ip_class = "B"
        ip_range = "128.0.0.0 - 191.255.255.255"

    elif first <= 223:
        ip_class = "C"
        ip_range = "192.0.0.0 - 223.255.255.255"

    elif first <= 239:
        ip_class = "D (Multicast)"
        ip_range = "224.0.0.0 - 239.255.255.255"

    else:
        ip_class = "E (Experimental)"
        ip_range = "240.0.0.0 - 255.255.255.255"


    if ip.startswith("10.") or ip.startswith("192.168.") or (ip.startswith("172.") and 16 <= int(ip.split(".")[1]) <= 31):
        ip_type = "Private"
    else:
        ip_type = "Public"


    return {
        "class": ip_class,
        "type": ip_type,
        "range": ip_range
    }