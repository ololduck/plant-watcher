#!/usr/bin/env python

import sys
import os
import json
import datetime
import shutil

from flask import Flask, render_template


def check_reqs():
    error = False
    try:
        import flask
        flask  # shut up, linter
    except ImportError as e:
        print("error: flask could not been found. Please install \
flask via 'pip install flask'\n" + str(e))
        error = True
    if(not os.path.exists("static") or not os.path.isdir("static")):
        os.path.mkdir("static")
    if(not os.path.exists("static/archives") or not os.path.isdir(
            "static/archives")):
        os.path.mkdir("static/archives")
    if(error):
        exit(1)


def update_images():
    now = datetime.datetime.now()
    FORMAT = "%Y_%m_%d__%H"
    if(os.path.exists("static/current.jpg")):
        shutil.copy(
            os.path.abspath(os.getcwd()) + "/static/current.jpg",
            os.path.abspath(os.getcwd()) + "/static/archives/%s.jpg"
            % now.strftime(FORMAT)
        )

check_reqs()


def get_config(fname="plant_watcher.conf"):
    data = {}
    with open(fname, 'r') as f:
        data = json.loads(f.read())
    return data


conf = get_config()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", conf=conf)


@app.route('/archives/')
def archives():
    c = {}
    c["images"] = reversed(os.listdir('static/archives'))
    return render_template("archives.html", conf=conf, contexte=c)

if __name__ == '__main__':
    print("Starting plant_watcher...")
    for arg in sys.argv:
        if(arg == "update_images"):
            update_images()
            exit(0)
        if(arg == "--debug"):
            conf["debug"] = True
    if("debug" in conf):
        app.debug = conf["debug"]
    app.run(host='0.0.0.0')
