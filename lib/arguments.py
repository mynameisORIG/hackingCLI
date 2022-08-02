#!/usr/bin/python3

class argNmap():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", type=str, required=True, help="IP or hostname you wish to scan")
    args = parser.parse_args()