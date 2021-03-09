from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="toolgui",
    version="0.0.4",
    description="Simple event-driven Python GUI framework for building modular tools with ImGui.",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rempelj/toolgui",
    author="Justin Rempel",
    classifiers=["Development Status :: 1 - Planning"],
    install_requires=[
        "imgui[glfw]",
    ],
    extras_require={
        "dev": [
            "twine",
            "wheel",
        ],
    },
)
