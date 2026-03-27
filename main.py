from newtons_method import newtons_method
from multivariate_newtons_method import multivariate_newtons_method
import numpy as np
import numpy.polynomial.polynomial as poly
import math as m
from get_expressions import get_expressions

expressions_list, symbols_list, symbols_dict = get_expressions()

bound = 5

x = np.linspace(-bound,bound,500)
y = x

X, Y = np.meshgrid(x, y)

init_guesses = X + Y * 1j

rows = init_guesses.shape[0]
cols = init_guesses.shape[1]
convergence = np.zeros((rows,cols))
roots = []
iter_counts = np.zeros((rows,cols))
colors = np.zeros((rows,cols,3))
maxit = 2000
TOL = 1e-6

max_k = 0

for i in range(rows):
    for j in range(cols):
        init_guess = init_guesses[i,j]
        if len(symbols_list) > 1:
            expr = expressions_list[0]
            var = symbols_list[0]
            converged, root, k = multivariate_newtons_method(init_guess, maxit, TOL, expr, var)
        else:
            expr = expressions_list[0]
            var = symbols_list[0]
            converged, root, k = newtons_method(init_guess, maxit, TOL, symbols_list, symbols_dict)
        if converged == True:
            for b,r in enumerate(roots):
                if abs(root - r) < TOL:
                    #print("no new roots to append")
                    convergence[i,j] = b
                    iter_counts[i,j] = k
                    if k > max_k:
                        max_k = k
                    break
            else:
                #print("adding root to list")
                roots.append(root)
                convergence[i,j] = len(roots) - 1 
                iter_counts[i,j] = k

        else:
            convergence[i,j] = np.nan
            
print(roots)
scaled_iter_counts = 1/np.max(iter_counts) * iter_counts
scaled_convergence = convergence + scaled_iter_counts
