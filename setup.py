"""Set up the project."""
# Standard library
from typing import List
from typing import Sequence

# Third-party
from pkg_resources import parse_requirements
from setuptools import find_packages
from setuptools import setup


def read_present_files(paths: Sequence[str]) -> str:
    """Read the content of those files that are present."""
    contents: List[str] = []
    for path in paths:
        try:
            with open(path, "r") as f:
                contents += ["\n".join(map(str.strip, f.readlines()))]
        except FileNotFoundError:
            continue
    return "\n\n".join(contents)


description_files = [
    "README",
    "README.rst",
    "README.md",
    "HISTORY",
    "HISTORY.rst",
    "HISTORY.md",
]

metadata = {
    "name": "pytrajplot",
    "version": "1.1.1",
    "description": "Michel Zeller's pytrajplot",
    "long_description": read_present_files(description_files),
    "author": "Michel Zeller",
    "author_email": "michel.zeller@meteoswiss.ch",
    "url": "https://github.com/mizeller/pytrajplot",
    "keywords": "pytrajplot",
    "classifiers": [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
}

python = ">= 3.7"

# Runtime dependencies (unpinned: only critical version restrictions)
with open("requirements/requirements.txt") as f:
    requirements = list(map(str, parse_requirements(f.readlines())))

scripts = [
    "pytrajplot=pytrajplot.cli:main",
]

setup(
    python_requires=python,
    install_requires=requirements,
    entry_points={"console_scripts": scripts},
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_save=False,
    **metadata,
)
