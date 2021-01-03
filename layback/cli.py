#!/usr/bin/env python

from .archive import Archive
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-url",
                        help="the URL of the resource you want to download.", required=True)
    parser.add_argument("-d",
                        help="directory to save the files.", required=True)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    if args.d.endswith('/') is False:
        args.d += '/'
    archive = Archive(args.url, args.d)
    archive.initialize()

if __name__ == "__main__":
    main()
