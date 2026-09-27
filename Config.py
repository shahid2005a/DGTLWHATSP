#!/usr/bin/env python3
"""
Central configuration for the project.
Import this in serve.py, tunnel.py, or any other module.
"""

import os
from pathlib import Path

# ------------------------------------------------------------------
# Project paths
# ------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR              # folder served by serve.py
WHATSAPP_HTML = BASE_DIR / "whatsapp.html"

# ------------------------------------------------------------------
# HTTP Server (serve.py)
# ------------------------------------------------------------------
SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))
SERVER_REUSE_ADDR = True
SERVER_DIRECTORY = str(STATIC_DIR)   # root directory to serve

# ------------------------------------------------------------------
# Tunnel (tunnel.py)
# ------------------------------------------------------------------
NGROK_AUTHTOKEN = os.getenv("NGROK_AUTHTOKEN", "")   # set via env or paste here
TUNNEL_PORT = SERVER_PORT            # port to expose
TUNNEL_PROTOCOL = "http"             # "http" or "tcp"

# ------------------------------------------------------------------
# WhatsApp (whatsapp.html)
# ------------------------------------------------------------------
# Country code + number, NO "+", spaces, or dashes.
# Example: India -> "919876543210"
WHATSAPP_DEFAULT_NUMBER = os.getenv("WA_NUMBER", "919999999991")

# Demo contacts shown in the sidebar
WHATSAPP_CONTACTS = [
    {"name": "Alice", "number": "919999999991", "msg": "Hey there! 👋", "time": "10:24"},
    {"name": "Bob",   "number": "919999999992", "msg": "See you tomorrow", "time": "09:15"},
    {"name": "Carol", "number": "919999999993", "msg": "Thanks!", "time": "Yesterday"},
    {"name": "David", "number": "919999999994", "msg": "Sent a photo", "time": "Yesterday"},
]

# ------------------------------------------------------------------
# App / misc
# ------------------------------------------------------------------
APP_NAME = "MyServer"
DEBUG = os.getenv("DEBUG", "1") == "1"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# ------------------------------------------------------------------
# Optional: pretty print when run directly
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("=== config.py ===")
    print(f"BASE_DIR        : {BASE_DIR}")
    print(f"STATIC_DIR      : {STATIC_DIR}")
    print(f"SERVER_HOST     : {SERVER_HOST}")
    print(f"SERVER_PORT     : {SERVER_PORT}")
    print(f"NGROK_AUTHTOKEN : {'(set)' if NGROK_AUTHTOKEN else '(not set)'}")
    print(f"TUNNEL_PROTOCOL : {TUNNEL_PROTOCOL}")
    print(f"DEBUG           : {DEBUG}")
    print(f"LOG_LEVEL       : {LOG_LEVEL}")
    print(f"Contacts        : {len(WHATSAPP_CONTACTS)}")