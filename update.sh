#!bin/bash

jupyter-book build docs/
ghp-import -n -p -c xai4se.github.io -f docs/_build/html