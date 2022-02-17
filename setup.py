import setuptools

import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        readme = stream.read().decode("utf8")


setuptools.setup(
    name="postale",
    version="0.1.0",
    author="gully",
    author_email="igully@gmail.com",
    description="A Python package for modeling diffraction gratings",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Echelle/postale",
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    packages=setuptools.find_packages(where="src", exclude=["data/*, paper/*, notebooks/*"]),
    package_dir={"": "src"},
    package_data={
        # If any package contains *.txt files, include them:
        "": ["*.csv"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
