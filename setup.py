import setuptools

with open('README.md', 'r') as f:
    readme = f.read()

setuptools.setup(
    name = "MojangAPI",
    version = "0.0.3",
    author = "Jack92829",
    description = "An async python wrapper for Mojangs API and Authentication API",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Jack92829/Mojang-API-Wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    project_urls={
        "Issue tracker": "https://github.com/Jack92829/Mojang-API-Wrapper/issues",
        "Documentation": "https://github.com/Jack92829/Mojang-API-Wrapper/blob/master/Docs.md"
    }
) 
