"""Example `webopencv` application, with some bells and whistles.

Equivalent to `aiortc` example, using `webopencv` utilities.

https://github.com/aiortc/aiortc/tree/main/examples/server
"""

import argparse
import logging
import ssl

import webopencv as wcv


app = wcv.WebApplication(framerate=5)


@app.transform('Cartoon')
def cartoon(img, frame):
    return wcv.transforms.cartoon(img, frame)


@app.transform('Edge Detection')
def edge_detection(img, frame):
    return wcv.transforms.edge_detection(img, frame)


@app.transform('Rotate')
def rotate(img, frame):
    return wcv.transforms.rotate(img, frame)


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

    # spit out all logs if asked to
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # setup ssl
    if args.cert_file:
        ssl_context = ssl.SSLContext()
        ssl_context.load_cert_chain(args.cert_file, args.key_file)
    else:
        ssl_context = None

    # launch app
    app.run(access_log=None, port=args.port, ssl_context=ssl_context)