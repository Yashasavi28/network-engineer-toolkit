from fastapi.middleware.cors import CORSMiddleware # type: ignore
from fastapi import FastAPI # type: ignore
from tools.subnet import calculate_subnet
from tools.bgp import generate_bgp_config
from tools.iprange import calculate_ip_range
from tools.cidr import summarize_networks
from tools.ipv6 import calculate_ipv6

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
    return calculate_subnet(network)

@app.get("/bgp")
def bgp(local_as: int, neighbor_ip: str, peer_as: int):
    return generate_bgp_config(local_as, neighbor_ip, peer_as)

@app.get("/iprange")
def iprange(start_ip: str, end_ip: str):
    return calculate_ip_range(start_ip, end_ip)

@app.get("/cidr")
def cidr(networks: str):

    net_list = networks.split(",")

    return summarize_networks(net_list)

@app.get("/ipv6")
def ipv6(network: str):
    return calculate_ipv6(network)