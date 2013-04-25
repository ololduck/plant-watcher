#!/usr/bin/env python

import sys
import os
import json
import datetime
import shutil

from flask import Flask, render_template


def get_config(fname="plant_watcher.conf"):
    data = {}
    with open(fname, 'r') as f:
        data = json.loads(f.read())
    return data


def update_images():
    now = datetime.datetime.now()
    FORMAT = "%Y_%M_%d__%H_%m_%S"
    if(os.path.exist("static/current.jpg")):
        shutil.copyfile(
            "static/current.jpg",
            "static/archives/%s.jpg" % now.strfrtime(FORMAT)
        )


conf = get_config()

app = Flask(__name__)


@app.route('/')
def home():
    c = {}
    c["images"] = os.listdir('static')
    return render_template("home.html", conf=conf, contexte=c)


@app.route('/archives/')
def archives():
    c = {}
    c["images"] = os.listdir('static/archives')
    return render_template("archives.html", conf=conf, contexte=c)

if __name__ == '__main__':
    print("Starting plant_watcher...")
    for arg in sys.argv:
        if(arg == "update_images"):
            update_images()
            exit(0)
    if("debug" in conf):
        app.debug = conf["debug"]
    app.run(host='0.0.0.0')
