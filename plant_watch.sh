#!/bin/bash

PROJECT_DIR=$HOME/plant_watcher

cd $PROJECT_DIR
PID=$(cat plant_watcher.pid)
kill $PID
python plant_watcher.py &
echo $! > plant_watcher.pid

