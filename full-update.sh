#!bin/bash

# delete branch locally
git branch -D gh-pages

# delete branch remotely
git push origin --delete gh-pages

# re-build a jupyter book and push gh-pages
jupyter-book build docs/
ghp-import -n -p -c xai4se.github.io -f docs/_build/html