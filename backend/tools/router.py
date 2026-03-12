from fastapi import APIRouter
from fastapi.responses import FileResponse
import os
import json

router = APIRouter()

FRONTEND_DIR = "frontend"

with open(os.path.join(FRONTEND_DIR, "tools.json")) as f:
    TOOLS = json.load(f)

# Create fast slug lookup
SLUG_MAP = {tool["slug"]: tool for tool in TOOLS.values()}


@router.get("/")
def homepage():
    return FileResponse(
        os.path.join(FRONTEND_DIR, "index.html")
    )


@router.get("/{tool_slug}")
def load_tool(tool_slug: str):

    tool = SLUG_MAP.get(tool_slug)

    if tool:
        return FileResponse(
            os.path.join(FRONTEND_DIR, tool["file"])
        )

    return FileResponse(
        os.path.join(FRONTEND_DIR, "404.html")
    )