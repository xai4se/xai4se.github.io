#!bin/bash

rm -rf docs/_build
# re-build a jupyter book and push gh-pages
jupyter-book build docs/
ghp-import -n -p -c xai4se.github.io -f docs/_build/html