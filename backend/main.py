from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.tools.router import router

from backend.tools.subnet import calculate_subnet
from backend.tools.cidr import summarize_networks
from backend.tools.iprange import calculate_ip_range
from backend.tools.vlsm import calculate_vlsm
from backend.tools.wildcard import calculate_wildcard
from backend.tools.ipconvert import ip_to_binary
from backend.tools.ipclass import detect_ip_class
from backend.tools.ipv6 import calculate_ipv6
from backend.tools.reversedns import reverse_dns

from backend.tools.broadcast import calculate_broadcast
from backend.tools.prefix import prefix_to_mask
from backend.tools.subnetviz import subnet_visualizer

from backend.tools.dnslookup import dns_lookup
from backend.tools.whoislookup import whois_lookup
from backend.tools.asnlookup import asn_lookup

from backend.tools.portlookup import port_lookup
from backend.tools.mtu import mtu_calculator
from backend.tools.tcpwindow import tcp_window
from backend.tools.latency import latency_calc
from backend.tools.bandwidth import bandwidth_calc


app = FastAPI()

# -----------------------------
# CORS
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Static frontend folders
# -----------------------------

app.mount("/assets", StaticFiles(directory="frontend/assets"), name="assets")
app.mount("/layout", StaticFiles(directory="frontend/layout"), name="layout")

# -----------------------------
# Include router (HTML pages)
# -----------------------------

app.include_router(router)

# -----------------------------
# Tool usage tracking
# -----------------------------

tool_usage = {}

visitors = 0


# -----------------------------
# API endpoints
# -----------------------------

@app.get("/subnet")
def subnet(network: str):
    return calculate_subnet(network)


@app.get("/cidr")
def cidr(networks: str):
    net_list = networks.split(",")
    return summarize_networks(net_list)


@app.get("/iprange")
def iprange(start_ip: str, end_ip: str):
    return calculate_ip_range(start_ip, end_ip)


@app.get("/vlsm")
def vlsm(network: str, hosts: str):
    return calculate_vlsm(network, hosts)


@app.get("/wildcard")
def wildcard(mask: str):
    return calculate_wildcard(mask)


@app.get("/ipconvert")
def ipconvert(ip: str):
    return ip_to_binary(ip)


@app.get("/ipclass")
def ipclass(ip: str):
    return detect_ip_class(ip)


@app.get("/ipv6")
def ipv6(network: str):
    return calculate_ipv6(network)


@app.get("/reversedns")
def reversedns(ip: str):
    return reverse_dns(ip)


@app.get("/broadcast")
def broadcast(network: str):
    return calculate_broadcast(network)


@app.get("/prefix")
def prefix(prefix: int):
    return prefix_to_mask(prefix)


@app.get("/subnetviz")
def subnetviz(network: str):
    return subnet_visualizer(network)


@app.get("/dnslookup")
def dnslookup(domain: str):
    return dns_lookup(domain)


@app.get("/whois")
def whois(domain: str):
    return whois_lookup(domain)


@app.get("/asn")
def asn(ip: str):
    return asn_lookup(ip)


@app.get("/port")
def port(port: int):
    return port_lookup(port)


@app.get("/mtu")
def mtu(mtu: int):
    return mtu_calculator(mtu)


@app.get("/tcpwindow")
def tcpwindow(bandwidth: int, latency: int):
    return tcp_window(bandwidth, latency)

@app.get("/latency")
def latency(distance: int):
    return latency_calc(distance)


@app.get("/bandwidth")
def bandwidth(size: int, speed: int):
    return bandwidth_calc(size, speed)


# -----------------------------
# Visitor counter
# -----------------------------

@app.get("/visit")
def visit():
    global visitors
    visitors += 1
    return {"visitors": visitors}