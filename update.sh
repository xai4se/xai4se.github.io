#!bin/bash

rm -rf docs/_build
# re-build a jupyter book and push gh-pages
jupyter-book build docs/
