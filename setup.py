try:
    from setuptools import setup #type: ignore
except ImportError:
    from distutils.core import setup


with open("README.md") as readme_file:
    readme_string = readme_file.read()

setup(
    name="toml-tools",
    version="0.10.6",
    description="A fork of toml, a Python Library for TOML",
    author="William Pearson, James Parrott",  
    author_email="james.parrott@proton.me",
    url="https://github.com/JamesParrott/toml_tools",
    # packages=['toml_tools'],
    license="MIT",
    long_description=readme_string,
    long_description_content_type = 'text/markdown',
    python_requires=">=2.6, !=3.0.*, !=3.1.*, !=3.2.*",
    classifiers=[
        'Development Status :: 3 - Alpha', #5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
