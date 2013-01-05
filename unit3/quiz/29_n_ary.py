# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 
from functools import update_wrapper

def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        return f(x) if not args else f(x, n_ary_f(*args))
    # for debugging convenience
    update_wrapper(n_ary_f, f)
    return n_ary_f

# the same as:
# seq = n_ary(seq)
@n_ary
def seq(x, y): return ('seq', x, y)

help(seq)
