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
import math 
import streamlit as st
import numpy as np


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

grade_job = my_new_df_jobs['Manager']['Learning']
#print(grade_job)

grade_applicant = my_new_df_app['Josh']['Communication']
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
#print(lst)

def fitting(lst,my_new_df_app,my_new_df_jobs):
    res_val=0.0 
    for comp in my_new_df_app[lst[0]]:
        mult = my_new_df_app[unique_applist[0]][comp]* my_new_df_jobs[unique_joblist[1]][comp]
        if math.isnan(mult):
            mult=0.0
        res_val=res_val + mult
    return res_val


def utility(lst,my_new_df_app,my_new_df_jobs):
    res_util=0.0
    for comb in lst:
        res_util=res_util + fitting(comb,my_new_df_app,my_new_df_jobs)
    return res_util

#print(utility)

def naive_approach(lst,my_new_df_app,my_new_df_jobs):
    max=0.0
    max_perm_element=(None,None)
    for l in lst:
        val=utility(l,my_new_df_app,my_new_df_jobs)
        if val > max:
            ress=val
            ress_tpl=l
    return [ress,ress_tpl]

print(naive_approach(lst,my_new_df_app,my_new_df_jobs))

st.title("A software system for automatically selecting suitable candidates according to their qualifications ")
def home(applicants,jobs,my_df_jobs,my_df_applicants):
    st.header('Home page')
    st.write(applicants,jobs,my_df_jobs,my_df_applicants)
def example_1(my_df_jobs):
    st.header('Example Requirements:')
    st.write(my_df_jobs)
def applicants_1(my_df_applicants):
    st.header('Example Applicants:')
    st.write(my_df_applicants)
st.sidebar.title("Navigation")
options = st.sidebar.radio('Pages',options=['Home','Requirements example','Applicants example',])

if options == 'Home':
    home(applicants,jobs,my_df_jobs,my_df_applicants)
elif options == 'Requirements example':
    example_1(my_df_jobs)
elif options == 'Applicants example':
    applicants_1(my_df_applicants)

uploaded_file = st.file_uploader('Upload you file here')

if uploaded_file:
    data=pd.read_csv(uploaded_file)
    st.write(data)
    
matrix_app = np.matrix(applicants)
#print(matrix_app)


