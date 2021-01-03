# Layback Machine

Creates an animated GIF from a given URLs history via the Wayback Machine. Depending on the age of your site, it may take some considerable time to process.

```sh
layback -url example.com -d /Downloads/
```

## Dependencies

[PhantomJS](http://phantomjs.org/), [Selenium](https://pypi.python.org/pypi/selenium), [imageio](https://pypi.python.org/pypi/imageio)

## Installation

Use [pip](https://pypi.python.org/pypi/pip):
```
pip install layback
```

## Usage

```
layback [-h] -url URL -d D

optional arguments:
  -h, --help  show this help message and exit
  -url URL    the URL of the resource you want to download.
  -d D        directory to save the files.
```