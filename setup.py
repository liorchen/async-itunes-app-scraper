import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="async-itunes-app-scraper-dmi",
    version="0.9.5",
    author="liorchen",
    author_email="liorchen2@gmail.com",
    description="A lightweight async iTunes App Store scraper based on https://github.com/digitalmethodsinitiative/itunes-app-scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liorchen/async-itunes-app-scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp>=3.5.2,<4.0'
    ],
    python_requires='>=3.6',
)