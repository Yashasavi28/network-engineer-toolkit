from fastapi.middleware.cors import CORSMiddleware # type: ignore
from fastapi import FastAPI # type: ignore
from tools.subnet import calculate_subnet
from tools.bgp import generate_bgp_config
from tools.iprange import calculate_ip_range
from tools.cidr import summarize_networks
from tools.ipv6 import calculate_ipv6
from tools.vlsm import calculate_vlsm
from tools.wildcard import calculate_wildcard
from tools.ipconvert import ip_to_binary
from tools.reversedns import reverse_dns

tool_usage = {
    "subnet": 0,
    "iprange": 0,
    "cidr": 0,
    "ipv6": 0,
    "bgp": 0
}
total_visits = 0

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message": "Network Engineer Toolkit API running"}

@app.get("/subnet")
def subnet(network: str):

    tool_usage["subnet"] += 1

    return calculate_subnet(network)

@app.get("/bgp")
def bgp(local_as: int, neighbor_ip: str, peer_as: int):

    tool_usage["bgp"] += 1

    return generate_bgp_config(local_as, neighbor_ip, peer_as)

@app.get("/iprange")
def iprange(start_ip: str, end_ip: str):

    tool_usage["iprange"] += 1

    return calculate_ip_range(start_ip, end_ip)

@app.get("/cidr")
def cidr(networks: str):

    tool_usage["cidr"] += 1

    net_list = networks.split(",")

    return summarize_networks(net_list)

@app.get("/ipv6")
def ipv6(network: str):

    tool_usage["ipv6"] += 1

    return calculate_ipv6(network)

@app.get("/vlsm")
def vlsm(network: str, hosts: str):

    tool_usage["vlsm"] = tool_usage.get("vlsm", 0) + 1

    return calculate_vlsm(network, hosts)

@app.get("/wildcard")
def wildcard(mask: str):

    tool_usage["wildcard"] = tool_usage.get("wildcard", 0) + 1

    return calculate_wildcard(mask)

@app.get("/ipconvert")
def ipconvert(ip: str):

    tool_usage["ipconvert"] = tool_usage.get("ipconvert", 0) + 1

    return ip_to_binary(ip)

@app.get("/reversedns")
def reversedns(ip: str):

    tool_usage["reversedns"] = tool_usage.get("reversedns", 0) + 1

    return reverse_dns(ip)

@app.get("/stats")
def stats():

    global total_visits

    total_visits = sum(tool_usage.values())

    return {
        "tools": tool_usage,
        "total_visits": total_visits
    }
    
visitors = 0

@app.get("/visit")
def visit():

    global visitors

    visitors += 1

    return {"visitors": visitors}