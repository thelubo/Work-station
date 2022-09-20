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

import sys


applicants = pd.read_csv ('applicants.csv')
jobs = pd.read_csv ('jobs.csv')


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
    print('----------------------------------------')    
    print(my_new_df_app)
    for comp in my_new_df_app[lst[0]]:
        print(comp)
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
    max=0.0
    max_perm_element=(None,None)
    for l in lst:
        val=utility(l,my_new_df_app,my_new_df_jobs)
        if val > max:
            ress=val
            ress_tpl=l
    return [ress,ress_tpl]

print('NA : ',)
print(naive_approach(lst,my_new_df_app,my_new_df_jobs))


#
import numpy as np

grades = {}
for i in my_new_df_app:
    grades[i] = {}
    for j in my_new_df_jobs:
        grades[i][j] = fitting(tuple((i,j)),my_new_df_app,my_new_df_jobs)

m = np.array([[grades[app][job] for job in sorted(grades[app])] for app in sorted(grades)])
maxn = m.max() + 1.0
print(m)

print('lsa---------------------')
from scipy.optimize import linear_sum_assignment

row_ind, col_ind = linear_sum_assignment(m, maximize=True)
sum_val = m[row_ind, col_ind].sum()

print(row_ind, col_ind, sum_val)

print('munkres---------------------')
from munkres import Munkres, print_matrix



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

