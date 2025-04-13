from math import *

exec("print(dir())")
exec("print(dir())", {})
exec("print(factorial(5))", {"factorial": factorial})
exec("print(fact(5))", {"fact": factorial})

prog = 'print("The sum of 5 and 10 is", (5+10))'
exec(prog)

x = 'print(55)'
eval(x)

func = '5 + 5'
print(exec(func))
print(eval(func))