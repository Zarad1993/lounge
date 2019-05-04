try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("lounge/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \'(.*?)\'", f.read()).group(1)

setup(
    name="lounge",
    version=version,
    author="Mohammad Albakri",
    author_email="mohammad.albakri93@gmail.com",
    packages=find_packages(),
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Zarad1993/lounge",
    install_requires=[
        "click==7.0",
        "pyyaml>=4.2b1",
        "gitpython==2.1.11",
        "watchdog==0.9.0",
        "pytest==4.4.0"
        ],
    entry_points = {
        "console_scripts": ["lounge"],
    },
    package_data={
        '': ['*.yaml'],
    },
)
