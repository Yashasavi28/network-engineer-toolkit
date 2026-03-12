import ipaddress

def subnet_visualizer(network):

    net = ipaddress.ip_network(network, strict=False)

    prefix = net.prefixlen

    return {
        "network": str(net.network_address),
        "prefix": prefix,
        "network_bits": prefix,
        "host_bits": 32 - prefix
    }