
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GooglePlayStoreScrape",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Apurva Sijaria",                     # Full name of the author
    description="GooglePlayStoreScrape Package for Scraping Play Store Reviews",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    url="https://github.com/apurvasijaria/GooglePlayStoreScrape",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.7',                # Minimum version requirement of the package
    py_modules=["GooglePlayStoreScrape"],             # Name of the python package
    package_dir={'':'GooglePlayStoreScrape/src'},     # Directory of the source code of the package
    install_requires=['chromedriver_binary==91.0.4472.101.0','pandas','selenium','bs4']                     # Install other dependencies if any
)

