from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from tools.subnet import calculate_subnet
from tools.bgp import generate_bgp_config
from tools.iprange import calculate_ip_range

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