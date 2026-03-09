import ipaddress

def summarize_networks(networks):

    net_list = [ipaddress.ip_network(n) for n in networks]

    summary = ipaddress.collapse_addresses(net_list)

    return {
        "summary": [str(net) for net in summary]
    }