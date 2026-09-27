#!/usr/bin/env python3
"""
Tunnel a local port to the internet using ngrok.
Requires an ngrok auth token (free at https://dashboard.ngrok.com/get-started/your-authtoken).

Usage:
    python tunnel.py              # tunnels localhost:8000
    python tunnel.py 5000         # tunnels localhost:5000
    python tunnel.py 5000 YOUR_TOKEN
"""

import sys
import time
import os

try:
    from pyngrok import ngrok
except ImportError:
    print("pyngrok is not installed. Run: pip install pyngrok")
    sys.exit(1)


def main():
    PORT = 8000
    AUTH_TOKEN = os.environ.get("NGROK_AUTHTOKEN", "")

    # Parse arguments
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port: {sys.argv[1]}")
            sys.exit(1)

    if len(sys.argv) > 2:
        AUTH_TOKEN = sys.argv[2]

    # Set auth token if provided
    if AUTH_TOKEN:
        ngrok.set_auth_token(AUTH_TOKEN)
    else:
        print("Warning: No auth token provided. Set NGROK_AUTHTOKEN env var")
        print("or pass it as a second argument.")
        print("Get one free at: https://dashboard.ngrok.com/get-started/your-authtoken\n")

    # Open the tunnel
    print(f"Opening tunnel to localhost:{PORT} ...")
    tunnel = ngrok.connect(PORT, "http")

    print(f"\n✅ Public URL: {tunnel.public_url}")
    print(f"   Forwarding to: http://localhost:{PORT}")
    print("\nPress Ctrl+C to stop the tunnel.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClosing tunnel...")
        ngrok.disconnect(tunnel.public_url)
        ngrok.kill()
        print("Tunnel closed.")


if __name__ == "__main__":
    main()