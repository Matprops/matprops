from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='matprops',
    version='1.0.0',
    description='Python library written on top of matplotlib library for customizable proportional charts',
    py_modules=['matprops'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "numpy >= 1.22.0",
        "pandas >= 1.3.5",
        "matplotlib >= 3.5.1"
    ],
    extras_require={
        "dev": [
            "pytest >= 6.2.5"
        ]
    },
    url="https://github.com/sharajmohamars/matprops",
    author="Mohammed Shammeer",
    author_email="sharajmohamars@gmail.com"
)
