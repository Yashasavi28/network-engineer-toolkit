import ipaddress

def summarize_networks(networks):

    net_list = []

    for n in networks:
        net_list.append(ipaddress.ip_network(n.strip()))

    summary = list(ipaddress.collapse_addresses(net_list))

    return {
        "summary": [str(net) for net in summary]
    }