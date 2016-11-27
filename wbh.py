#!/usr/bin/env python3


""" Open the web browser with a HTTP query """

import sys
import argparse
import webbrowser
from flask import Flask, request, abort


""" Web server """
app = Flask(__name__)
default_port = 5000
default_host = '127.0.0.1'


@app.route("/open", methods=['POST'])
def open():
    url = request.form['url']
    print("Open url '%s'" % url)
    webbrowser.open(url)
    return ''

""" Main """


def main(arguments):
    parser = argparse.ArgumentParser('wbh', description=__doc__)
    parser.add_argument('--host', '-o',
                        help="Listening host (%s by default)" % default_host,
                        default=default_host,
                        required=False)
    parser.add_argument('--port', '-p',
                        help="Listening port number (%s by default)" % default_port,
                        type=int,
                        default=default_port,
                        required=False)
    args = parser.parse_args(arguments)

    app.run(
        host=args.host,
        port=int(args.port)
    )


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
