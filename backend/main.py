from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from backend.tools.subnet import calculate_subnet
from backend.tools.bgp import generate_bgp_config
from backend.tools.iprange import calculate_ip_range
from backend.tools.cidr import summarize_networks
from backend.tools.ipv6 import calculate_ipv6
from backend.tools.vlsm import calculate_vlsm
from backend.tools.wildcard import calculate_wildcard
from backend.tools.ipconvert import ip_to_binary
from backend.tools.reversedns import reverse_dns
from backend.tools.ipclass import detect_ip_class
from backend.tools.interface import generate_interface_config


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
# Serve frontend assets
# -----------------------------

app.mount("/assets", StaticFiles(directory="frontend/assets"), name="assets")


# -----------------------------
# Tool usage tracking
# -----------------------------

tool_usage = {
    "subnet": 0,
    "iprange": 0,
    "cidr": 0,
    "ipv6": 0,
    "bgp": 0,
    "vlsm": 0,
    "wildcard": 0,
    "ipconvert": 0,
    "reversedns": 0,
    "ipclass": 0,
    "interface": 0
}

total_visits = 0
visitors = 0


# -----------------------------
# Serve frontend pages
# -----------------------------

@app.get("/")
def serve_home():
    response = FileResponse("frontend/index.html")
    response.headers["Cache-Control"] = "no-cache"
    return response


@app.get("/{page_name}.html")
def serve_page(page_name: str):

    file_path = f"frontend/{page_name}.html"

    if os.path.exists(file_path):
        return FileResponse(file_path)

    return {"error": "Page not found"}


# -----------------------------
# API endpoints
# -----------------------------

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

    tool_usage["vlsm"] += 1

    return calculate_vlsm(network, hosts)


@app.get("/wildcard")
def wildcard(mask: str):

    tool_usage["wildcard"] += 1

    return calculate_wildcard(mask)


@app.get("/ipconvert")
def ipconvert(ip: str):

    tool_usage["ipconvert"] += 1

    return ip_to_binary(ip)


@app.get("/reversedns")
def reversedns(ip: str):

    tool_usage["reversedns"] += 1

    return reverse_dns(ip)


@app.get("/ipclass")
def ipclass(ip: str):

    tool_usage["ipclass"] += 1

    return detect_ip_class(ip)


@app.get("/interface")
def interface(interface: str, ip: str, mask: str, description: str):

    tool_usage["interface"] += 1

    return generate_interface_config(interface, ip, mask, description)


# -----------------------------
# Stats API
# -----------------------------

@app.get("/stats")
def stats():

    global total_visits

    total_visits = sum(tool_usage.values())

    return {
        "tools": tool_usage,
        "total_visits": total_visits
    }


# -----------------------------
# Visitor counter
# -----------------------------

@app.get("/visit")
def visit():

    global visitors

    visitors += 1

    return {"visitors": visitors}

# -----------------------------
# Tool tracking API
# -----------------------------

@app.get("/track")
def track(tool: str):

    if tool in tool_usage:
        tool_usage[tool] += 1

    return {"status": "tracked", "tool": tool}