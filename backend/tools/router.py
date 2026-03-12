from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path
import json

router = APIRouter()

# project root
BASE_DIR = Path(__file__).resolve().parents[2]

# frontend folder
FRONTEND_DIR = BASE_DIR / "frontend"

# load tools.json
with open(FRONTEND_DIR / "tools.json") as f:
    TOOLS = json.load(f)


# -----------------------------
# Homepage
# -----------------------------

@router.get("/")
def homepage():
    return FileResponse(FRONTEND_DIR / "index.html")


# -----------------------------
# Dynamic Tool Loader
# -----------------------------

@router.get("/{tool_slug}")
def load_tool(tool_slug: str):

    for tool in TOOLS.values():

        if tool["slug"] == tool_slug:

            return FileResponse(
                FRONTEND_DIR / tool["file"]
            )

    return FileResponse(
        FRONTEND_DIR / "404.html"
    )