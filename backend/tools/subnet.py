import ipaddress

def calculate_subnet(network):
    net = ipaddress.ip_network(network, strict=False)

    return {
        "network_address": str(net.network_address),
        "broadcast_address": str(net.broadcast_address),
        "total_hosts": net.num_addresses
    }