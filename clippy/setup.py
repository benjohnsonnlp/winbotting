from setuptools import setup

setup(
    name="clippy",
    version="1.0.0",
    description="Get clipboard updates from discord",
    author="Ben Johnson",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=["clippy"],
    include_package_data=True,
    install_requires=[
        "feedparser", "html2text", "importlib_resources", "typing"
    ],
    entry_points={"console_scripts": ["clippy=clippy:main"]},
)