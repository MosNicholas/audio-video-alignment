#!/usr/bin/env sh

TOOLS=./build/tools

$TOOLS/caffe train --solver=siamese_solver.prototxt
