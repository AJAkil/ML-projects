from graph import *
import sys
import copy
import os


file_name = input('Enter the name of the file please: ')
method = input('Enter Number of the coloring method please!\
    Methods includes: \n 1. Degree Sorted \n 2. Random Ordering \n 3. DSature\n')
choice = ''

if method == '1':
    choice = 'degree_sorted'
elif method == '2':
    choice = 'random'
elif method == '3':
    choice = 'default'

f = open(os.path.join('.\\test_cases',file_name),'r+')
sol_name = file_name.split('.')[0]
sol = open(f'{sol_name}.sol','a+')
g = Graph()
g.construct_graph(f)

#g.greedy_color(choice=choice)
g.dsatur_algo_eff()
g.cal_avg_penalty(f)
g.print_result(f)
#g.write_to_file(sol)

# g.cal_avg_penalty(f)
# g.print_result(f)

g.operate_kempe_chain()

g.cal_avg_penalty(f)
g.print_result(f)




            