# FunctionRayTracer.py
#
# Basic ray tracer
#
# Version 0.1
#
# November 2014
# By David Lister
# 

from sympy import *
from sympy.abc import x

# Parameter and equations
X_MIN = -5
X_MAX = 5
STEP = 1

##f = 0.05 * x**2 # Parabola
f = -sqrt(10 **2 - x **2) + 10 # circle radius of 10
df = diff(f, x)

# Functions

def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

# Plotting

flist = (f,)
Functions = []

for i in drange(X_MIN, 0, STEP):
    n = 1.0/df.subs(x, i)
    m = float(tan(pi/2 - 2 * atan(float(n))))
    b = f.subs(x, i)- m * i
    flist = flist + (m * x + b,)
    Functions.append(m * x + b)

for i in drange(1, X_MAX +1, STEP):
    n = 1.0/df.subs(x, i)
    m = tan(pi/2 - 2 * atan(n))
    b = f.subs(x, i)- m * i
    flist = flist + (m * x + b,)
    Functions.append(m * x + b)
    

tally = 0
for function in Functions:
    tally += function.subs(x, 0)

print
print 'Average focal point is ' + str(float(tally /len(Functions)))
print

a = 'plot(' + str(flist)[1:-1] + ')' ## Very cumbersum, should be fixed when time is available
eval(a)
