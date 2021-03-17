#!/bin/bash
if [ ! "$(which python| grep anaconda)" ]; then
    echo ERROR: conda activate base
    exit
fi


jupyter-book build --overwrite .
jupyter-book build .
git add _build/*

git submodule update --remote Evaluacion_2020-2
