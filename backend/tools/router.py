from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

# mapping between url and html file
TOOLS = {
    "subnet-calculator": "subnet.html",
    "cidr-summarization": "cidr.html",
    "ipv6-subnet-calculator": "ipv6.html",
    "ip-range-calculator": "iprange.html",
    "vlsm-calculator": "vlsm.html",
    "wildcard-mask-calculator": "wildcard.html",
    "ip-to-binary-converter": "ipconvert.html",
    "reverse-dns-generator": "reversedns.html",
    "ip-class-detector": "ipclass.html",
    "bgp-config-generator": "bgp.html",
    "interface-config-generator": "interface.html",
}

FRONTEND_DIR = "frontend"


@router.get("/")
def homepage():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))


@router.get("/{tool_name}")
def load_tool(tool_name: str):

    if tool_name in TOOLS:
        return FileResponse(
            os.path.join(FRONTEND_DIR, TOOLS[tool_name])
        )

    return {"detail": "Not Found"}