import z3
import itertools
import numpy as np
## See https://en.wikipedia.org/wiki/Verbal_arithmetic
## cute: http://mathforum.org/library/drmath/view/60417.html

vars = dict()
def _mk_int_var (x):
    if x not in vars:
        vars[x] = z3.Int (str(x))
    return vars[x]

def mk_var (x):
    return _mk_int_var (x)

def get_vars ():
    return vars.values ()


def solve (s1, s2, s3):
    vars = {}
    solver = z3.Solver()
    for word in [s1, s2, s3]:
      for v in word:
        if v not in vars:
          vars[v] = z3.Int(v)
	  solver.add(vars[v] >= 0)
	  solver.add(vars[v] <= 9)

    val_a = reduce(lambda x,y: 10*x+vars[y], s1, 0)
    val_b = reduce(lambda x,y: 10*x+vars[y], s2, 0)
    val_c = reduce(lambda x,y: 10*x+vars[y], s3, 0)
    solver.add(vars[s1[0]] != 0)
    solver.add(vars[s2[0]] != 0)
    solver.add(vars[s3[0]] != 0)
    solver.add(val_a + val_b == val_c)
    solver.add(z3.Distinct(vars.values()))
    
    if solver.check() == z3.sat:
      model = solver.model()
      print("The value of each letter for given words is calculated as:")
      print([(v, model[vars[v]]) for v in s1])

      init_const = 0.1

      for len_i in range(len(s1)):
	init_const = init_const * 10

      first_word = 0

      for vs1 in s1:
	vars_val = model[vars[vs1]]	
	vv = vars_val.as_long()
	first_word = first_word + int(vv * init_const)
	init_const = init_const/10
	
      #print(first_word)

      print([(v,model[vars[v]]) for v in s2])

      for len_i in range(len(s2)):
	init_const = init_const * 10

      second_word = 0

      for vs2 in s2:
	vars_val = model[vars[vs2]]	
	vv = vars_val.as_long()
	second_word = second_word + int(vv * init_const)
	init_const = init_const/10
	
      #print(second_word)

      print([(v,model[vars[v]]) for v in s3])

      for len_i in range(len(s3)):
	init_const = init_const * 10

      resultant_word = 0

      for vs3 in s3:
	vars_val = model[vars[vs3]]	
	vv = vars_val.as_long()
	resultant_word = resultant_word + int(vv * init_const)
	init_const = init_const/10
	
      #print(resultant_word)

      if first_word + second_word == resultant_word:		
	return first_word, second_word, resultant_word
      
    else:
      print("failed to solve")

    # Replace with your solution
    pass


def print_sum (s1, s2, s3):
    s1 = str(s1)
    s2 = str(s2)
    s3 = str(s3)
    print s1.rjust (len(s3) + 1)
    print '+'
    print s2.rjust (len(s3) + 1)
    print ' ' + ('-'*(len(s3)))
    print s3.rjust (len(s3) + 1)
    
def puzzle (s1, s2, s3):
    print("\nVerbal Arithmetic puzzle is:")
    print_sum (s1, s2, s3)
    print("\n")
    res = solve (s1, s2, s3)
    if res is None:
        print 'No solution'
    else:
        print '\nSolution:'
	print (res[0], res[1], res[2])
	print("\n")
	print ("Verbal Arithmetic Sum values are:")
        print_sum (res[0], res[1], res[2])
        
if __name__ == '__main__':
    puzzle ('SEND', 'MORE', 'MONEY')
    
