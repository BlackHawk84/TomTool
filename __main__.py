#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from TomTool.main import main

parser = argparse.ArgumentParser(description='TOM Tool')
parser.add_argument('-c', type=str, metavar='file', dest='conf',
                    help='configuration file')
args = parser.parse_args()

main(args)
