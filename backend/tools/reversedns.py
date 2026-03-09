def reverse_dns(ip):

    parts = ip.split(".")

    reversed_ip = ".".join(reversed(parts))

    ptr = reversed_ip + ".in-addr.arpa"

    return {
        "ptr_record": ptr
    }