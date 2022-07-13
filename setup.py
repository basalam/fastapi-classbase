import setuptools

with open("readme.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "faclassbase",
    version = "0.1.0",
    author = "omidekz",
    author_email = "omidekz@gmail.com",
    description = "FastAPI class-base API",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/omidekz/fastapi-classbase",
    project_urls = {
        "Bug Tracker": "https://github.com/omidekz/fastapi-classbase/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "faclassbase"},
    packages = setuptools.find_packages(where="faclassbase"),
    python_requires = ">=3.6"
)
