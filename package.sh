#!/bin/bash

script_dir=$(dirname "$0")
cd "$script_dir" || exit

rm -rf build
rm -rf dist

python setup.py sdist bdist_wheel

twine upload dist/*
