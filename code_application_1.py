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
from scipy.optimize import linear_sum_assignment
from munkres import Munkres
import sys


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
        mult = my_new_df_app[lst[0]][comp]* my_new_df_jobs[lst[1]][comp]
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
    ress=0.0
    for l in lst:
        val=utility(l,my_new_df_app,my_new_df_jobs)
        if val > ress:
            ress=val
            ress_tpl=l
    return [ress,ress_tpl]

print(naive_approach(lst,my_new_df_app,my_new_df_jobs))

l=2


grades = {}
for i in my_new_df_app:
    grades[i] = {}
    for j in my_new_df_jobs:
        grades[i][j] = fitting(tuple((i,j)),my_new_df_app,my_new_df_jobs)

m = np.array([[grades[app][job] for job in sorted(grades[app])] for app in sorted(grades)])
maxn = m.max() + 1.0
print(m)

print('lsa---------------------')

row_ind, col_ind = linear_sum_assignment(m, maximize=True)
sum_val = m[row_ind, col_ind].sum()

print(row_ind, col_ind, sum_val)

print('munkres---------------------')

from munkres import print_matrix


m_lst = (maxn -m).tolist()

munk = Munkres()

indexes = munk.compute(m_lst)
print(indexes)
print_matrix(m_lst, msg='Lowest cost through this matrix:')
total = 0
for row, column in indexes:
    value = m_lst[row][column]
    total += value
    print(f'({row}, {column}) -> {value}')
print('total cost: ',total)

print('munkres2---------------------')


matrix = m.tolist()
cost_matrix = []

for row in matrix:
    cost_row = []
    for col in row:
        cost_row += [maxn - col]
    cost_matrix += [cost_row]

munk = Munkres()
indexes = munk.compute(cost_matrix)
print_matrix(matrix, msg='Highest profit through this matrix:')
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    print(f'({row}, {column}) -> {value}')

print(f'total profit={total}')

st.title("A software system for automatically selecting suitable candidates according to their qualifications ")
def home(applicants,jobs):
    st.header('Home page')
    st.write(applicants,jobs)
def Load(my_df_jobs,my_df_applicants):
    st.header("Load Dataframes:")
    dataframes_select = st.selectbox("Please select a Dataframe",options = ["Applicants","Jobs"])
    if dataframes_select == "Applicants":
        st.write(my_df_applicants)
    elif dataframes_select == "Jobs":
        st.write(my_df_jobs)
    dataframes_select = st.selectbox("Please select a Dataframe",options = ["Jobs","Applicants"])
    if dataframes_select == "Applicants":
        st.write(my_df_applicants)
    elif dataframes_select == "Jobs":
        st.write(my_df_jobs)
    algorithm_select = st.selectbox("Please select an Algorithm",options = ["Naive approache","Munkres","LSA"])
    if algorithm_select == "Naive approache":
        st.write(naive_approach(lst,my_new_df_app,my_new_df_jobs))
    elif algorithm_select == "Munkres":
        st.write(total)
    elif algorithm_select == "LSA":
        st.write(total)
def example_1(my_df_jobs):
    st.header('View Jobs Dataframe:')
    st.write(my_df_jobs)
def applicants_1(my_df_applicants):
    st.header('View Applicants Dataframe:')
    st.write(my_df_applicants)
st.sidebar.title("Navigation")
options = st.sidebar.radio('Pages',options=['Home','Load Dataframes','View Jobs Dataframe','View Applicants Dataframe',])

if options == 'Home':
    home(applicants,jobs)
elif options == 'Load Dataframes':
    Load(my_df_jobs, my_df_applicants)
elif options == 'View Jobs Dataframe':
    example_1(my_df_jobs)
elif options == 'View Applicants Dataframe':
    applicants_1(my_df_applicants)

uploaded_file = st.file_uploader('Upload you file here')

if uploaded_file:
    data=pd.read_csv(uploaded_file)
    st.write(data)
