#!/usr/bin/env python3
"""
Simple HTTP server to serve files from the current directory.
Usage:
    python serve.py            # serves on port 8000
    python serve.py 8080       # serves on custom port
    python serve.py 8080 0.0.0.0  # custom port and host
"""

import http.server
import socketserver
import sys
import os

def main():
    # Default values
    PORT = 8000
    HOST = "0.0.0.0"

    # Parse command-line arguments
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port: {sys.argv[1]}")
            sys.exit(1)

    if len(sys.argv) > 2:
        HOST = sys.argv[2]

    # Change to the script's directory (optional)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    Handler = http.server.SimpleHTTPRequestHandler

    # Allow port reuse to avoid "Address already in use" errors
    socketserver.TCPServer.allow_reuse_address = True

    try:
        with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
            print(f"Serving HTTP on {HOST}:{PORT} ...")
            print(f"Open http://localhost:{PORT}/ in your browser")
            print("Press Ctrl+C to stop.\n")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except OSError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()