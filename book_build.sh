#!/bin/bash
#conda activate base
jupyter-book build --overwrite .
jupyter-book build .
git add _build/*

git submodule update --remote Evaluacion_2020-2
