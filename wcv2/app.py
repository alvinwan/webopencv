"""
Originally from `aiortc` example. With modifications for wcv2.

https://github.com/aiortc/aiortc/tree/main/examples/server
"""

import argparse
import logging
import ssl

from .aio import app


def get_ssl_context(cert_file, key_file):
    if not cert_file or not key_file:
        return None
    ssl_context = ssl.SSLContext()
    ssl_context.load_cert_chain(cert_file, key_file)
    return ssl_context


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="WebRTC audio / video / data-channels demo"
    )
    parser.add_argument("--cert-file", help="SSL certificate file (for HTTPS)")
    parser.add_argument("--key-file", help="SSL key file (for HTTPS)")
    parser.add_argument(
        "--port", type=int, default=8080, help="Port for HTTP server (default: 8080)"
    )
    parser.add_argument("--verbose", "-v", action="count")
    args = parser.parse_args()

    # extra setup
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    ssl_context = get_ssl_context(args.cert_file, args.key_file)

    # launch app
    app.run(access_log=None, port=args.port, ssl_context=ssl_context)
