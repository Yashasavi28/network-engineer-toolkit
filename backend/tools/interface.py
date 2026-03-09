def generate_interface_config(interface, ip, mask, description):

    cisco = f"""
interface {interface}
 description {description}
 ip address {ip} {mask}
 no shutdown
"""

    juniper = f"""
set interfaces {interface} description "{description}"
set interfaces {interface} unit 0 family inet address {ip}/{mask}
"""

    arista = f"""
interface {interface}
 description {description}
 ip address {ip}/{mask}
 no shutdown
"""

    return {
        "cisco": cisco.strip(),
        "juniper": juniper.strip(),
        "arista": arista.strip()
    }