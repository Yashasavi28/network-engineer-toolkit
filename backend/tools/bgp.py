def generate_bgp_config(local_as, neighbor_ip, peer_as):

    config = f"""
set routing-options autonomous-system {local_as}
set protocols bgp group EBGP type external
set protocols bgp group EBGP neighbor {neighbor_ip} peer-as {peer_as}
"""

    return {
        "config": config
    }