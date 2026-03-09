import ipaddress
import math

def calculate_vlsm(network, hosts):

    net = ipaddress.IPv4Network(network)

    host_list = [int(h) for h in hosts.split(",")]
    host_list.sort(reverse=True)

    results = []

    current_network = net.network_address

    for host in host_list:

        needed = host + 2

        prefix = 32 - math.ceil(math.log2(needed))

        subnet = ipaddress.IPv4Network(f"{current_network}/{prefix}", strict=False)

        results.append(str(subnet))

        current_network = subnet.broadcast_address + 1

    return {
        "subnets": results
    }