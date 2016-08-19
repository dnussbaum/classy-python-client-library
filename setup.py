from setuptools import setup

setup(
    name="classyclient",
    version="1.0.0",
    description="A package for interacting with Classy's API in Python.",
    url="https://github.com/dnussbaum/classy-python-client-library",
    author="Daniel Nussbaum",
    author_email="daniel.e.nussbaum@gmail.com",
    license="MIT",
    packages=["classyclient"],
	install_requires=[
        "requests",
    ],
    zip_safe=True
)
