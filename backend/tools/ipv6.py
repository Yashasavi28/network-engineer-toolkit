import ipaddress

def calculate_ipv6(network):

    net = ipaddress.IPv6Network(network, strict=False)

    return {
        "network_address": str(net.network_address),
        "prefix_length": net.prefixlen,
        "num_addresses": net.num_addresses
    }