# Layback Machine

Layback Machine is a command-line tool that creates an animated gif of a given URLs history via the Wayback Machine.

```sh
layback google.com /Downloads/
```

## Dependencies

[PhantomJS](http://phantomjs.org/), [Selenium](https://pypi.python.org/pypi/selenium), [imageio](https://pypi.python.org/pypi/imageio)

## Installation

```
pip install layback_machine
```

## Usage

```
layback [-h] -url URL -d D

optional arguments:
  -h, --help  show this help message and exit
  -url URL    the URL of the resource you want to download.
  -d D        directory to save the files.
```

## Support

Currently only supports Python 2.
