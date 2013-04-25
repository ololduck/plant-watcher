#!/usr/bin/env python

import sys
import os
import json

from flask import Flask, url_for, render_template


def get_config(fname=__name__+".conf"):
    data = {}
    with open(fname, 'r') as f:
        data = json.loads(f.read())
    return data


conf = get_config()

app = Flask(__name__)

@app.route('/')
def home():
    c = {}
    c["images"] = os.listdir('.')
    return render_template("home.html", contexte=c)


if __name__ == '__main__':
    app.run()
