import ipaddress


def prefix_to_mask(prefix: int):

    net = ipaddress.IPv4Network(f"0.0.0.0/{prefix}")

    return {
        "prefix": prefix,
        "subnet_mask": str(net.netmask)
    }