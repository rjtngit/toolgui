from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="toolgui",
    version="0.0.0",
    description="toolgui",
    package_dir={"": "toolgui"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rempelj/toolgui",
    author="Justin Rempel",
    author_email="justinrempel@gmail.com",
    classifiers=["Development Status :: 1 - Planning"],
    install_requires=[
        "imgui[glfw]",
    ],
)