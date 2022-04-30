from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="toolgui",
    version="0.0.9",
    description="Modular event-driven GUI system for quickly building tools with Python and pyimgui.",
    packages=find_packages(),
    package_data={'': ['Roboto-Regular.ttf']},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rempelj/toolgui",
    author="Justin Rempel",
    classifiers=[
    ],
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
