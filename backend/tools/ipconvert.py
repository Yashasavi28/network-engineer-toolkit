def ip_to_binary(ip):

    parts = ip.split(".")

    binary_parts = []

    for p in parts:
        binary_parts.append(format(int(p), "08b"))

    return {
        "binary": ".".join(binary_parts)
    }