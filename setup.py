import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="karel-python",
    version="0.0.1",
    author="Linar Khilazhev",
    author_email="zzlinarzz@gmail.com",
    description="Karel realisation on python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/linzer0/karel-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
