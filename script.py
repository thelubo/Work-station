# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:54:58 2022

@author: thelu
"""

import pandas
import argparse

Jobs = pandas.read_csv('D:\Jobs.csv')
print(Jobs)

parser = argparse.ArgumentParser( description ='Viewing the contents of Jobs.csv')
parser.add_argument("file", type=argparse.FileType('r'), help="This will display the contents of the job file")
args = parser.parse_args()
with args.file as file:
    print(file.read())
#options = parser.parse_args()







