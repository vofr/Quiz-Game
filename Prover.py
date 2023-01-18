
import os
import time
suspects=[[0 for _ in range(3)] for _ in range(6)]
suspects[0] = ['v(a)', 'v(ah)', 'v(s)', 'v(d)', 'v(ab)']
suspects[1] = ['m(a)&m(c)','m(b)&m(e)','m(a)&m(e)&p(b)&i(c)&i(d)']
suspects[2] = ['d(s)&d(b)','d(ma)&d(r)','d(ma)&d(mi)']


def puzzle(i,j):
 rowToChange = 0 #select which row from theoremX.in to change
 if (i == 1): rowToChange = 98
 elif (i == 2): rowToChange = 59
 else : rowToChange=18

 fileIn = 'theorem' + str(i) + '.in'
 fileOut = 'theorem' + str(i) + '.out'
 sysOperation = "prover9 <" + fileIn + '>' + fileOut

 answer=False
 os.chdir(r"Prover9-Mace4\bin-win32")
 formulas = 'formulas(goals).\n'
 assumption = suspects[i-1][j] + '.\n'
 endof = 'end_of_list.\n'
 replace_line(fileIn, rowToChange, formulas)
 replace_line(fileIn, rowToChange+1, assumption)
 replace_line(fileIn, rowToChange+2, endof)
 os.system(sysOperation)
 time.sleep(1)
 answer=searchInFile(fileOut,'THEOREM PROVED', 'SEARCH FAILED')
 os.chdir(r"..")
 os.chdir(r"..")
 return answer

def replace_line(file_name, line_num, text):
 lines = open(file_name, 'r').readlines()
 lines[line_num] = text
 out = open(file_name, 'w')
 out.writelines(lines)
 out.close()

def searchInFile(file_name,correctAnswer,wrongAnswer):
 with open(file_name, "r") as file:
  for line_number, line in enumerate(file, start=1):
   if correctAnswer in line:
    return True
   if wrongAnswer in line:
    return False