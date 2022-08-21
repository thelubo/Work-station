# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 12:31:17 2022

@author: thelu
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:54:58 2022

@author: thelu
"""

import pandas
import argparse

Applicants = pandas.read_csv('D:\Applicants.csv')
Jobs = pandas.read_csv('D:\Jobs.csv')
#print(Jobs)
#print("\n")
#print(Applicants)

parser = argparse.ArgumentParser( description ='Viewing the contents of Jobs.csv')
parser.add_argument("-file", type = int, help="This will display the contents of the file depending on the number: 1-Jobs(displays Jobs)\n 2-Applicants(displays Applicants) \n 3-Both Jobs and Applicants(displays both Jobs and Applicants)")
args = parser.parse_args()    

if args.file == 1:
    print("\n")
    print(Jobs)
    print("\n")
elif args.file == 2:
    print("\n")
    print(Applicants)
    print("\n")
elif args.file == 3:
    print("\n")
    print(Jobs)
    print("\n")
    print(Applicants)
    print("\n")

dict_from_csv_applicant = pandas.read_csv('D:\Applicants.csv').to_dict()
#print(dict_from_csv_applicant)

from itertools import permutations
a = permutations ([dict_from_csv_applicant])
for i in a:
    print(i)

#options = parser.parse_args()







