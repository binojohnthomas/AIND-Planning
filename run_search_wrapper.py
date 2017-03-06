from  run_search import *
import os

search_list= [10]

problem_list =[1,2,3]

for problem in problem_list:
    for search in search_list:
        arg1 = str(problem)
        arg2 = str(search)
        python_exe = "python run_search.py -p " +arg1+ " -s " + arg2
        print (python_exe)
        os.system(python_exe)


