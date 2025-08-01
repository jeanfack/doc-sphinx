#!/bin/bash -x

SCRIPT_DIR=$(dirname "$0")

cd $SCRIPT_DIR

git add *

git add -u

git commit -m "update"

git push origin main
