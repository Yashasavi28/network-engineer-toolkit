import ipaddress

def calculate_ip_range(start_ip, end_ip):

    start = ipaddress.IPv4Address(start_ip)
    end = ipaddress.IPv4Address(end_ip)

    total_ips = int(end) - int(start) + 1

    return {
        "start_ip": start_ip,
        "end_ip": end_ip,
        "total_ips": total_ips
    }