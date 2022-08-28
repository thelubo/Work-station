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

import pandas as pd
import argparse
import itertools
from itertools import permutations


applicants = pd.read_csv ('D:\Applicants.csv')
jobs = pd.read_csv ('D:\Jobs.csv')
#print(jobs)
#print("\n")
#print(applicants)

parser = argparse.ArgumentParser( description ='Viewing the contents of jobs.csv')
parser.add_argument("-file", type = int, help="This will display the contents of the file depending on the number: 1-Jobs(displays Jobs)\n 2-Applicants(displays Applicants) \n 3-Both Jobs and Applicants(displays both Jobs and Applicants)")
args = parser.parse_args()    

if args.file == 1:
    print("\n")
    print(jobs)
    print("\n")
elif args.file == 2:
    print("\n")
    print(applicants)
    print("\n")
elif args.file == 3:
    print("\n")
    print(jobs)
    print("\n")
    print(applicants)
    print("\n")

#dict_from_csv_applicant = pd.read_csv('D:\Applicants.csv').to_dict()
#print(dict_from_csv_applicant)

#from itertools import permutations
#a = permutations ([dict_from_csv_applicant])
#for i in a:
#    print(i)

my_df_applicants= applicants.pivot(index='skill name',columns= 'applicant name',values = 'grade')
#print(my_df_applicants)

my_new_df_app = my_df_applicants.to_dict('dict')
#print(my_new_df_app)

my_df_jobs = jobs.pivot(index='skill name',columns ='job name', values='grade')
#print(my_df_jobs)

my_new_df_jobs = my_df_jobs.to_dict('dict')
#print(my_new_df_jobs)

#grade_job = my_new_df_jobs['Manager']['Learning']
#print(grade_job)

#grade_applicant = my_new_df_app['Josh']['Communication']
#print(grade_applicant)

unique_applicants = set(my_new_df_app)
unique_applist=list(unique_applicants)
#print(unique_applist)

unique_jobs = set(my_new_df_jobs)
unique_joblist=list(unique_jobs)
#print(unique_joblist)

uniq_app_perm =  list(permutations(unique_applist))
#print(uniq_app_perm)

lst=[]
for i in uniq_app_perm:
    lst.append(tuple(zip(i,unique_joblist)))
print(lst)
