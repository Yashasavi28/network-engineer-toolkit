import ipaddress

def calculate_broadcast(network):

    net = ipaddress.ip_network(network, strict=False)

    return {
        "network": str(net.network_address),
        "broadcast": str(net.broadcast_address),
        "hosts": net.num_addresses
    }