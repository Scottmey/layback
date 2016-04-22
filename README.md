# Layback Machine

Layback Machine is a command-line tool that creates an animated gif of a given URLs history via the Wayback Machine. Depending on the age of your site, it may take some considerable time to process.

```sh
layback -url google.com -d /Downloads/
```

## Dependencies

[PhantomJS](http://phantomjs.org/), [Selenium](https://pypi.python.org/pypi/selenium), [imageio](https://pypi.python.org/pypi/imageio)

## Installation

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

## Support

Supports both Python 2 & 3.

## Example Output
![movie](https://cloud.githubusercontent.com/assets/969752/14750417/bb214ef2-0892-11e6-9a01-71c9824c9f3e.gif)

